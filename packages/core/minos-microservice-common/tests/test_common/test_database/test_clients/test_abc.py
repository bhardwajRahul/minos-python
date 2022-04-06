import unittest
from abc import (
    ABC,
)
from typing import (
    Any,
    AsyncIterator,
)
from unittest.mock import (
    AsyncMock,
    MagicMock,
    call,
)

from minos.common import (
    AiopgDatabaseClient,
    BuildableMixin,
    DatabaseClient,
    DatabaseClientBuilder,
)
from tests.utils import (
    CommonTestCase,
    FakeAsyncIterator,
)


class _DatabaseClient(DatabaseClient):
    """For testing purposes."""

    async def _is_valid(self, **kwargs) -> bool:
        """For testing purposes."""

    async def _reset(self, **kwargs) -> None:
        """For testing purposes."""

    async def _execute(self, *args, **kwargs) -> None:
        """For testing purposes."""

    def _fetch_all(self, *args, **kwargs) -> AsyncIterator[Any]:
        """For testing purposes."""


class TestDatabaseClient(unittest.IsolatedAsyncioTestCase):
    def test_abstract(self):
        self.assertTrue(issubclass(DatabaseClient, (ABC, BuildableMixin)))
        expected = {"_is_valid", "_execute", "_fetch_all", "_reset"}
        # noinspection PyUnresolvedReferences
        self.assertEqual(expected, DatabaseClient.__abstractmethods__)

    def test_get_builder(self):
        self.assertIsInstance(DatabaseClient.get_builder(), DatabaseClientBuilder)

    async def test_is_valid(self):
        mock = AsyncMock(side_effect=[True, False])
        client = _DatabaseClient()
        client._is_valid = mock

        self.assertEqual(True, await client.is_valid())
        self.assertEqual(False, await client.is_valid())

        self.assertEqual([call(), call()], mock.call_args_list)

    async def test_reset(self):
        mock = AsyncMock()
        client = _DatabaseClient()
        client._reset = mock

        await client.reset()

        self.assertEqual([call()], mock.call_args_list)

    async def test_execute(self):
        mock = AsyncMock()
        client = _DatabaseClient()
        client._execute = mock

        await client.execute("foo")

        self.assertEqual([call("foo")], mock.call_args_list)

    async def test_fetch_all(self):
        mock = MagicMock(return_value=FakeAsyncIterator(["one", "two"]))
        client = _DatabaseClient()
        client._fetch_all = mock

        self.assertEqual(["one", "two"], [v async for v in client.fetch_all()])

        self.assertEqual([call()], mock.call_args_list)

    async def test_fetch_one(self):
        mock = MagicMock(return_value=FakeAsyncIterator(["one", "two"]))
        client = _DatabaseClient()
        client._fetch_all = mock

        self.assertEqual("one", await client.fetch_one())

        self.assertEqual([call()], mock.call_args_list)


class TestDatabaseClientBuilder(CommonTestCase):
    def test_with_name(self):
        builder = DatabaseClientBuilder(AiopgDatabaseClient).with_name("query")
        self.assertEqual({"name": "query"}, builder.kwargs)

    def test_with_config(self):
        builder = DatabaseClientBuilder(AiopgDatabaseClient).with_name("query").with_config(self.config)
        self.assertEqual({"name": "query"} | self.config.get_database_by_name("query"), builder.kwargs)

    def test_build(self):
        builder = DatabaseClientBuilder(AiopgDatabaseClient).with_name("query").with_config(self.config)
        client = builder.build()

        self.assertIsInstance(client, AiopgDatabaseClient)
        self.assertEqual(self.config.get_database_by_name("query")["database"], client.database)


if __name__ == "__main__":
    unittest.main()
