from typing import (
    Optional,
)

from minos.common import (
    CommandReply,
)

from ...context import (
    SagaContext,
)
from ...definitions import (
    SagaOperation,
)
from ...exceptions import (
    MinosSagaExecutorException,
    MinosSagaFailedExecutionStepException,
)
from ...messages import (
    SagaResponse,
)
from .local import (
    LocalExecutor,
)


class ResponseExecutor(LocalExecutor):
    """Response Executor class."""

    # noinspection PyUnusedLocal
    async def exec(
        self, operation: Optional[SagaOperation], context: SagaContext, reply: CommandReply, *args, **kwargs
    ) -> SagaContext:
        """Execute the operation.

        :param operation: Operation to be executed.
        :param context: Actual execution context.
        :param reply: Command Reply which contains the response.
        :param args: Additional positional arguments.
        :param kwargs: Additional named arguments.
        :return: An updated context instance.
        """
        if operation is None:
            return context

        try:
            response = SagaResponse(reply.data, reply.status)
            context = SagaContext(**context)  # Needed to avoid mutability issues.
            context = await self.exec_operation(operation, context, response)
        except MinosSagaExecutorException as exc:
            raise MinosSagaFailedExecutionStepException(exc.exception)

        return context
