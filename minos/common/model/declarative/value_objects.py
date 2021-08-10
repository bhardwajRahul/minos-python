"""
Copyright (C) 2021 Clariteia SL

This file is part of minos framework.

Minos framework can not be copied and/or distributed without the express permission of Clariteia SL.
"""
from collections.abc import (
    MutableSet,
)
from typing import (
    Any,
    Generic,
    Iterable,
    Iterator,
    NoReturn,
    Optional,
    TypeVar,
)

from ...exceptions import (
    MinosImmutableClassException,
)
from .abc import (
    DeclarativeModel,
)

T = TypeVar("T")


class ValueObject(DeclarativeModel):
    """Value Object class."""

    def __setattr__(self, key: str, value: Any):
        if key.startswith("_"):
            super().__setattr__(key, value)
        else:
            raise MinosImmutableClassException("modification of an immutable value object not allowed")


class ValueObjectSet(DeclarativeModel, MutableSet, Generic[T]):
    """Value Object Set class."""

    data: list[ValueObject]

    def __init__(self, data: Optional[Iterable[T]] = None, *args, **kwargs):
        if data is None:
            data = list()
        elif not isinstance(data, list):
            data = [value_obj for value_obj in data]
        super().__init__(data, *args, **kwargs)

    def add(self, value_obj: ValueObject) -> NoReturn:
        """Add an entity.
        :param value_obj: The value object to be added.
        :return: This method does not return anything.
        """
        self.data.append(value_obj)

    def discard(self, value_object: ValueObject) -> NoReturn:
        self.data.remove(value_object)

    def __contains__(self, value_object: ValueObject) -> bool:
        return value_object in self.data

    def __len__(self) -> int:
        return len(self.data)

    def __iter__(self) -> Iterator[T]:
        yield from self.data

    def __eq__(self, other):
        if isinstance(other, ValueObjectSet):
            return super().__eq__(other)
        if isinstance(other, list):
            return self.data == other
        return list(self) == other
