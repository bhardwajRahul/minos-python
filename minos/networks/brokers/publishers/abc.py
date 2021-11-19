from __future__ import (
    annotations,
)

import logging
from abc import (
    ABC,
)
from typing import (
    Any,
    Optional,
)
from uuid import (
    UUID,
)

from psycopg2.sql import (
    SQL,
)

from minos.common import (
    MinosConfig,
    PostgreSqlMinosDatabase,
)

from ..messages import (
    BrokerMessage,
    BrokerMessageStatus,
)

logger = logging.getLogger(__name__)


class BrokerPublisherSetup(PostgreSqlMinosDatabase):
    """Minos Broker Setup Class"""

    async def _setup(self) -> None:
        await self._create_broker_table()

    async def _create_broker_table(self) -> None:
        await self.submit_query(_CREATE_TABLE_QUERY, lock=hash("producer_queue"))


class BrokerPublisher(BrokerPublisherSetup, ABC):
    """Minos Broker Class."""

    ACTION: str = "command"  # FIXME

    def __init__(self, *args, service_name: str, **kwargs):
        super().__init__(*args, **kwargs)
        self.service_name = service_name

    @classmethod
    def _from_config(cls, *args, config: MinosConfig, **kwargs) -> BrokerPublisher:
        return cls(*args, service_name=config.service.name, **config.broker.queue._asdict(), **kwargs)

    # noinspection PyMethodOverriding
    async def send(
        self,
        data: Any,
        topic: str,
        status: Optional[BrokerMessageStatus] = None,
        saga: Optional[UUID] = None,
        reply_topic: Optional[str] = None,
        user: Optional[UUID] = None,
        **kwargs,
    ) -> int:
        """Send a ``CommandReply``.

        :param data: The data to be send.
        :param topic: Topic in which the message will be published.
        :param saga: Saga identifier.
        :param status: command status.
        :param reply_topic: TODO
        :param user: TODO
        :param kwargs: TODO
        :return: This method does not return anything.
        """

        message = BrokerMessage(
            topic=topic,
            data=data,
            saga=saga,
            status=status,
            reply_topic=reply_topic,
            user=user,
            service_name=self.service_name,
        )
        logger.info(f"Sending '{message!s}'...")
        return await self.enqueue(message.topic, message.avro_bytes)

    async def enqueue(self, topic: str, raw: bytes) -> int:
        """Send a sequence of bytes to the given topic.

        :param topic: Topic in which the bytes will be send.
        :param raw: Bytes sequence to be send.
        :return: The identifier of the message in the queue.
        """
        params = (topic, raw, self.ACTION)
        raw = await self.submit_query_and_fetchone(_INSERT_ENTRY_QUERY, params)
        await self.submit_query(_NOTIFY_QUERY)
        return raw[0]


_CREATE_TABLE_QUERY = SQL(
    "CREATE TABLE IF NOT EXISTS producer_queue ("
    "id BIGSERIAL NOT NULL PRIMARY KEY, "
    "topic VARCHAR(255) NOT NULL, "
    "data BYTEA NOT NULL, "
    "action VARCHAR(255) NOT NULL, "
    "retry INTEGER NOT NULL DEFAULT 0, "
    "created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(), "
    "updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW())"
)

_INSERT_ENTRY_QUERY = SQL("INSERT INTO producer_queue (topic, data, action) VALUES (%s, %s, %s) RETURNING id")

_NOTIFY_QUERY = SQL("NOTIFY producer_queue")
