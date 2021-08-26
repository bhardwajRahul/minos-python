"""minos.networks.abc.consumers module."""

from __future__ import (
    annotations,
)

import logging
from typing import (
    Any,
    NoReturn,
    Optional,
)

from aiokafka import (
    AIOKafkaConsumer,
)
from psycopg2.sql import (
    SQL,
    Identifier,
)

from minos.common import (
    BROKER,
)

from .setups import (
    HandlerSetup,
)

logger = logging.getLogger(__name__)


class Consumer(HandlerSetup):
    """
    Handler Server

    Generic insert for queue_* table. (Support Command, CommandReply and Event)

    """

    __slots__ = "_topics", "_broker", "__consumer"

    def __init__(self, topics: set[str], broker: Optional[BROKER] = None, consumer: Optional[Any] = None, **kwargs):
        super().__init__(**kwargs)
        self._topics = set(topics)
        self._broker = broker
        self.__consumer = consumer

    async def _setup(self) -> None:
        await super()._setup()
        await self._consumer.start()

    @property
    def topics(self) -> set[str]:
        """Topics getter.

        :return: A list of string values.
        """
        return self._topics

    def add_topic(self, topic: str) -> None:
        """Add a topic to the consumer's subscribed topics.

        :param topic: Name of the topic to be added.
        :return: This method does not return anything.
        """
        self._topics.add(topic)
        self._consumer.subscribe(topics=list(self._topics))

    def remove_topic(self, topic: str) -> None:
        """Remove a topic from the consumer's subscribed topics.

        :param topic: Name of the topic to be removed.
        :return: This method does not return anything.
        """
        self._topics.remove(topic)
        if len(self._topics):
            self._consumer.subscribe(topics=list(self._topics))
        else:
            self._consumer.unsubscribe()

    @property
    def _consumer(self) -> AIOKafkaConsumer:
        if self.__consumer is None:  # pragma: no cover
            self.__consumer = AIOKafkaConsumer(
                *self._topics, bootstrap_servers=f"{self._broker.host}:{self._broker.port}"
            )
        return self.__consumer

    async def _destroy(self) -> None:
        await self._consumer.stop()
        await super()._destroy()

    async def dispatch(self) -> NoReturn:
        """Perform a dispatching step.

        :return: This method does not return anything.
        """
        await self.handle_message(self._consumer)

    async def handle_message(self, consumer: Any) -> None:
        """Message consumer.

        It consumes the messages and sends them for processing.

        Args:
            consumer: Kafka Consumer instance (at the moment only Kafka consumer is supported).
        """

        async for message in consumer:
            await self.handle_single_message(message)

    async def handle_single_message(self, message):
        """Handle Kafka messages.

        Evaluate if the binary of message is an Event instance.
        Add Event instance to the event_queue table.

        Args:
            message: Kafka message.

        Raises:
            Exception: An error occurred inserting record.
        """
        logger.debug(f"Consuming message with {message.topic!s} topic...")

        return await self.queue_add(message.topic, message.partition, message.value)

    async def queue_add(self, topic: str, partition: int, binary: bytes) -> int:
        """Insert row to event_queue table.

        Retrieves number of affected rows and row ID.

        Args:
            topic: Kafka topic. Example: "TicketAdded"
            partition: Kafka partition number.
            binary: Event Model in bytes.

        Returns:
            Queue ID.

            Example: 12

        Raises:
            Exception: An error occurred inserting record.
        """
        queue_id = await self.submit_query_and_fetchone(
            _INSERT_QUERY.format(Identifier(self.TABLE_NAME)), (topic, partition, binary),
        )
        await self.submit_query(_NOTIFY_QUERY.format(Identifier(self.TABLE_NAME)))
        await self.submit_query(_NOTIFY_QUERY.format(Identifier(topic)))

        return queue_id[0]


_INSERT_QUERY = SQL(
    "INSERT INTO {} (topic, partition_id, binary_data, creation_date) VALUES (%s, %s, %s, NOW()) RETURNING id"
)

_NOTIFY_QUERY = SQL("NOTIFY {}")
