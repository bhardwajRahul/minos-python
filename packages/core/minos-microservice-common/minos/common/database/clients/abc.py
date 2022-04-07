from __future__ import (
    annotations,
)

from abc import (
    ABC,
    abstractmethod,
)
from collections.abc import (
    AsyncIterator,
)
from typing import (
    Any,
    Optional,
)

from minos.common.database.operations import DatabaseOperationFactory

from ...builders import (
    BuildableMixin,
    Builder,
)
from ...config import (
    Config,
)
from ..operations import (
    ComposedDatabaseOperation,
    DatabaseOperation,
)


class DatabaseClient(ABC, BuildableMixin):
    """Database Client base class."""

    _factories = dict()

    @classmethod
    def _from_config(cls, config: Config, name: Optional[str] = None, **kwargs) -> DatabaseClient:
        return super()._from_config(config, **config.get_database_by_name(name), **kwargs)

    async def is_valid(self, **kwargs) -> bool:
        """Check if the instance is valid.

        :return: ``True`` if it is valid or ``False`` otherwise.
        """
        return await self._is_valid(**kwargs)

    @abstractmethod
    async def _is_valid(self, **kwargs) -> bool:
        raise NotImplementedError

    async def reset(self, **kwargs) -> None:
        """Reset the current instance status.

        :param kwargs: Additional named parameters.
        :return: This method does not return anything.
        """
        return await self._reset(**kwargs)

    @abstractmethod
    async def _reset(self, **kwargs) -> None:
        raise NotImplementedError

    async def execute(self, operation: DatabaseOperation) -> None:
        """Execute an operation.

        :param operation: TODO
        :return: This method does not return anything.
        """
        if isinstance(operation, ComposedDatabaseOperation):
            for op in operation.operations:
                await self._execute(op)
        else:
            await self._execute(operation)

    @abstractmethod
    async def _execute(self, operation: DatabaseOperation) -> None:
        raise NotImplementedError

    async def fetch_one(self) -> Any:
        """Fetch one value.

        :return: This method does not return anything.
        """
        return await self.fetch_all().__anext__()

    def fetch_all(self) -> AsyncIterator[Any]:
        """Fetch all values with an asynchronous iterator.

        :return: This method does not return anything.
        """
        return self._fetch_all()

    @abstractmethod
    def _fetch_all(self, *args, **kwargs) -> AsyncIterator[Any]:
        raise NotImplementedError

    @classmethod
    def register_factory(cls, base: type[DatabaseOperationFactory], impl: type[DatabaseOperationFactory]) -> None:
        """TODO

        :param base: TODO
        :param impl: TODO
        :return:
        """
        if not issubclass(base, DatabaseOperationFactory):
            raise ValueError(f"{base!r} must be a subclass of {DatabaseOperationFactory!r}")

        if not issubclass(impl, base):
            raise ValueError(f"{impl!r} must be a subclass of {base!r}")

        cls._factories[base] = impl

    @classmethod
    def get_factory(cls, base: type[DatabaseOperationFactory]) -> DatabaseOperationFactory:
        """TODO

        :param base: TODO
        :return: TODO
        """
        return cls._factories[base]()


class DatabaseClientBuilder(Builder[DatabaseClient]):
    """Database Client Builder class."""

    def with_name(self, name: str) -> DatabaseClientBuilder:
        """Set name.

        :param name: The name to be added.
        :return: This method return the builder instance.
        """
        self.kwargs["name"] = name
        return self

    def with_config(self, config: Config) -> DatabaseClientBuilder:
        """Set config.

        :param config: The config to be set.
        :return: This method return the builder instance.
        """
        database_config = config.get_database_by_name(self.kwargs.get("name"))
        self.kwargs |= database_config
        return self


DatabaseClient.set_builder(DatabaseClientBuilder)
