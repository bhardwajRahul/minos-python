from __future__ import (
    annotations,
)

import logging
from typing import (
    TYPE_CHECKING,
    AsyncIterator,
    Optional,
)
from uuid import (
    UUID,
)

from ...exceptions import (
    MinosSnapshotAggregateNotFoundException,
)
from ...queries import (
    _Condition,
    _EqualCondition,
    _Ordering,
)
from ...transactions import (
    TransactionEntry,
)
from ...uuid import (
    NULL_UUID,
)
from ..entries import (
    SnapshotEntry,
)
from .abc import (
    PostgreSqlSnapshotSetup,
)
from .queries import (
    PostgreSqlSnapshotQueryBuilder,
)

if TYPE_CHECKING:
    from ...model import (
        Aggregate,
    )

logger = logging.getLogger(__name__)


class PostgreSqlSnapshotReader(PostgreSqlSnapshotSetup):
    """PostgreSQL Snapshot class.

   The snapshot provides a direct accessor to the aggregate instances stored as events by the event repository class.
    """

    async def get(self, aggregate_name: str, uuid: UUID, **kwargs) -> Aggregate:
        """Get an aggregate instance from its identifier.

        :param aggregate_name: Class name of the ``Aggregate``.
        :param uuid: Identifier of the ``Aggregate``.
        :param kwargs: Additional named arguments.
        :return: The ``Aggregate`` instance.
        """
        snapshot_entry = await self.get_entry(aggregate_name, uuid, **kwargs)
        aggregate = snapshot_entry.build_aggregate(**kwargs)
        return aggregate

    # noinspection PyUnusedLocal
    async def get_entry(self, aggregate_name: str, uuid: UUID, **kwargs) -> SnapshotEntry:
        """Get an ``SnapshotEntry`` from its identifier.

        :param aggregate_name: Class name of the ``Aggregate``.
        :param uuid: Identifier of the ``Aggregate``.
        :param kwargs: Additional named arguments.
        :return: The ``Aggregate`` instance.
        """

        try:
            return await self.find_entries(
                aggregate_name, _EqualCondition("uuid", uuid), **kwargs | {"exclude_deleted": False},
            ).__anext__()
        except StopAsyncIteration:
            raise MinosSnapshotAggregateNotFoundException(f"Some aggregates could not be found: {uuid!s}")

    async def find(self, *args, **kwargs) -> AsyncIterator[Aggregate]:
        """Find a collection of ``Aggregate`` instances based on a ``Condition``.

        :param args: Additional positional arguments.
        :param kwargs: Additional named arguments.
        :return: An asynchronous iterator that containing the ``Aggregate`` instances.
        """
        async for snapshot_entry in self.find_entries(*args, **kwargs):
            yield snapshot_entry.build_aggregate(**kwargs)

    async def find_entries(
        self,
        aggregate_name: str,
        condition: _Condition,
        ordering: Optional[_Ordering] = None,
        limit: Optional[int] = None,
        streaming_mode: bool = False,
        transaction: Optional[TransactionEntry] = None,
        exclude_deleted: bool = True,
        **kwargs,
    ) -> AsyncIterator[SnapshotEntry]:
        """Find a collection of ``SnapshotEntry`` instances based on a ``Condition``.

        :param aggregate_name: Class name of the ``Aggregate``.
        :param condition: The condition that must be satisfied by the ``Aggregate`` instances.
        :param ordering: Optional argument to return the instance with specific ordering strategy. The default behaviour
            is to retrieve them without any order pattern.
        :param limit: Optional argument to return only a subset of instances. The default behaviour is to return all the
            instances that meet the given condition.
        :param streaming_mode: If ``True`` return the values in streaming directly from the database (keep an open
            database connection), otherwise preloads the full set of values on memory and then retrieves them.
        :param transaction: TODO.
        :param exclude_deleted: If ``True``, deleted ``Aggregate`` entries are included, otherwise deleted ``Aggregate``
            entries are filtered.
        :param kwargs: Additional named arguments.
        :return: An asynchronous iterator that containing the ``Aggregate`` instances.
        """
        if transaction is None:
            transaction_uuids = (NULL_UUID,)
        else:
            transaction_uuids = await transaction.uuids

        qb = PostgreSqlSnapshotQueryBuilder(
            aggregate_name, condition, ordering, limit, transaction_uuids, exclude_deleted,
        )
        query, parameters = qb.build()

        async with self.cursor() as cursor:
            # noinspection PyTypeChecker
            await cursor.execute(query, parameters)
            if streaming_mode:
                async for row in cursor:
                    # noinspection PyArgumentList
                    yield SnapshotEntry(*row)
                return
            else:
                rows = await cursor.fetchall()
        for row in rows:
            yield SnapshotEntry(*row)
