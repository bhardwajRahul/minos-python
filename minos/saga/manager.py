"""
Copyright (C) 2021 Clariteia SL

This file is part of minos framework.

Minos framework can not be copied and/or distributed without the express permission of Clariteia SL.
"""
from __future__ import (
    annotations,
)

import logging
from uuid import (
    UUID,
)

from minos.common import (
    CommandReply,
    MinosConfig,
    MinosSagaManager,
    import_module,
)

from .definitions import (
    Saga,
)
from .exceptions import (
    MinosSagaFailedExecutionStepException,
    MinosSagaPausedExecutionStepException,
)
from .executions import (
    SagaExecution,
    SagaExecutionStorage,
)

logger = logging.getLogger(__name__)


def _build_definitions(items) -> dict[str, Saga]:
    def _fn(item) -> Saga:
        controller = import_module(item.controller)
        return getattr(controller, item.action)

    return {item.name: _fn(item) for item in items}


class SagaManager(MinosSagaManager):
    """Saga Manager implementation class.

    The purpose of this class is to manage the running process for new or paused``SagaExecution`` instances.
    """

    def __init__(self, storage: SagaExecutionStorage, definitions: dict[str, Saga], *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.storage = storage
        self.definitions = definitions

    @classmethod
    def _from_config(cls, *args, config: MinosConfig, **kwargs) -> SagaManager:
        """Build an instance from config.

        :param args: Additional positional arguments.
        :param config: Config instance.
        :param kwargs: Additional named arguments.
        :return: A new ``classmethod`` instance.
        """
        storage = SagaExecutionStorage.from_config(config=config, **kwargs)
        definitions = _build_definitions(config.saga.items)
        return cls(*args, storage=storage, definitions=definitions, **kwargs)

    async def _run_new(self, name: str, **kwargs) -> UUID:
        definition = self.definitions.get(name)
        execution = SagaExecution.from_saga(definition)
        return await self._run(execution, **kwargs)

    async def _load_and_run(self, reply: CommandReply, **kwargs) -> UUID:
        execution = self.storage.load(reply.saga_uuid)
        return await self._run(execution, reply=reply, **kwargs)

    async def _run(self, execution: SagaExecution, **kwargs) -> UUID:
        try:
            await execution.execute(**kwargs)
        except MinosSagaPausedExecutionStepException:
            self.storage.store(execution)
            return execution.uuid
        except MinosSagaFailedExecutionStepException as exc:
            logger.warning(f"The {execution.uuid!r} execution failed: {exc!r}")
            self.storage.store(execution)
            return execution.uuid
        except Exception as exc:
            logger.error(f"The {execution.uuid!r} execution failed unexpectedly: {exc!r}")
            raise exc

        self.storage.delete(execution)
        return execution.uuid
