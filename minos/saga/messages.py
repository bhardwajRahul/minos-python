from __future__ import (
    annotations,
)

from enum import (
    IntEnum,
)
from typing import (
    Any,
    Optional,
    Union,
)


class SagaRequest:
    """Saga Request class."""

    __slots__ = (
        "_target",
        "_content",
    )

    def __init__(self, target: str, content: Any):
        self._target = target
        self._content = content

    @property
    def target(self) -> str:
        """Get the target of the request.

        :return: A ``str`` instance.
        """
        return self._target

    # noinspection PyUnusedLocal
    async def content(self, **kwargs) -> Any:
        """Get the content of the request.

        :param kwargs: Additional named parameters.
        :return: The content of the request.
        """
        return self._content

    def __eq__(self, other: Any) -> bool:
        return isinstance(other, type(self)) and self._target == other._target and self._content == other._content

    def __repr__(self) -> str:
        return f"{type(self).__name__}({self._target!r}, {self._content!r})"

    def __hash__(self):
        return hash((self._target, self._content))


class SagaResponse:
    """Saga Response class."""

    __slots__ = (
        "_content",
        "_status",
    )

    def __init__(self, content: Any, status: Optional[Union[int, SagaResponseStatus]] = None):
        if status is None:
            status = SagaResponseStatus.SUCCESS
        if not isinstance(status, SagaResponseStatus):
            status = SagaResponseStatus.from_raw(status)

        self._content = content
        self._status = status

    # noinspection PyUnusedLocal
    async def content(self, **kwargs) -> Any:
        """Get the response content.

        :param kwargs: Additional named parameters.
        :return: The content of the response.
        """
        return self._content

    @property
    def ok(self) -> bool:
        """Check if the response is okay.

        :return: ``True`` if the response is okay
        """
        return self._status == SagaResponseStatus.SUCCESS

    @property
    def status(self) -> SagaResponseStatus:
        """Get the status code of the response.

        :return: A ``ResponseStatus`` instance.
        """
        return self._status

    def __eq__(self, other: Any) -> bool:
        return isinstance(other, type(self)) and self._content == other._content and self._status == other._status

    def __repr__(self) -> str:
        return f"{type(self).__name__}({self._content!r}, {self._status!r})"

    def __hash__(self):
        return hash((self._content, self._status))


class SagaResponseStatus(IntEnum):
    """Saga Response Status class."""

    SUCCESS = 200
    ERROR = 400
    SYSTEM_ERROR = 500

    @classmethod
    def from_raw(cls, raw: int) -> SagaResponseStatus:
        """Build a new instance from raw.

        :param raw: The raw representation of the instance.
        :return: A ``SagaResponseStatus`` instance.
        """
        return next(obj for obj in cls if obj.value == raw)
