"""
Copyright (C) 2021 Clariteia SL

This file is part of minos framework.

Minos framework can not be copied and/or distributed without the express permission of Clariteia SL.
"""
from __future__ import (
    annotations,
)

import logging
import typing as t
from abc import (
    abstractmethod,
)
from base64 import (
    b64decode,
    b64encode,
)

from ..exceptions import (
    EmptyMinosModelSequenceException,
    MinosModelException,
    MultiTypeMinosModelSequenceException,
)
from ..meta import (
    classproperty,
    property_or_classproperty,
    self_or_classmethod,
)
from ..protocol import (
    MinosAvroProtocol,
)
from .fields import (
    AvroSchemaEncoder,
    ModelField,
)

logger = logging.getLogger(__name__)

# def _process_aggregate(cls):
#     """
#     Get the list of the class arguments and define it as an AggregateField class
#     """
#     cls_annotations = cls.__dict__.get('__annotations__', {})
#     aggregate_fields = []
#     for name, type in cls_annotations.items():
#         attribute = getattr(cls, name, None)
#         aggregate_fields.append(
#             AggregateField(name=name, type=type, value=attribute)
#         )
#     setattr(cls, "_FIELDS", aggregate_fields)
#
#     # g get metaclass
#     meta_class = getattr(cls, "Meta", None)
#     if meta_class:
#         # meta class exist so get the information related
#         ...
#     return cls
#
#
# def aggregate(cls=None):
#     def wrap(cls):
#         return _process_aggregate(cls)
#
#     if cls is None:
#         return wrap
#
#     return wrap(cls)

T = t.TypeVar("T")


class Model(t.Generic[T]):
    """Base class for ``minos`` model entities."""

    _fields: dict[str, ModelField] = {}

    def __init__(self, fields: dict[str, ModelField] = None):
        """Class constructor.

        :param fields: Dictionary that contains the ``ModelField`` instances of the model indexed by name.
        """
        if fields is None:
            fields = dict()
        self._fields = fields

    @classmethod
    def from_avro_str(cls, raw: str, **kwargs) -> t.Union[T, list[T]]:
        """Build a single instance or a sequence of instances from bytes

        :param raw: A bytes data.
        :return: A single instance or a sequence of instances.
        """
        raw = b64decode(raw.encode())
        return cls.from_avro_bytes(raw, **kwargs)

    @classmethod
    @abstractmethod
    def from_avro_bytes(cls, raw: bytes, **kwargs) -> t.Union[T, list[T]]:
        """Build a single instance or a sequence of instances from bytes

        :param raw: A bytes data.
        :return: A single instance or a sequence of instances.
        """

    @classmethod
    def to_avro_str(cls, models: list[T]) -> str:
        """Create a bytes representation of the given object instances.

        :param models: A sequence of minos models.
        :return: A bytes object.
        """
        return b64encode(cls.to_avro_bytes(models)).decode()

    @classmethod
    def to_avro_bytes(cls, models: list[T]) -> bytes:
        """Create a bytes representation of the given object instances.

        :param models: A sequence of minos models.
        :return: A bytes object.
        """
        if len(models) == 0:
            raise EmptyMinosModelSequenceException("'models' parameter cannot be empty.")

        model_type = type(models[0])
        if not all(model_type == type(model) for model in models):
            raise MultiTypeMinosModelSequenceException(
                f"Every model must have type {model_type} to be valid. Found types: {[type(model) for model in models]}"
            )

        avro_schema = models[0].avro_schema
        # noinspection PyTypeChecker
        return MinosAvroProtocol().encode([model.avro_data for model in models], avro_schema)

    @property
    def fields(self) -> dict[str, ModelField]:
        """Fields getter"""
        return self._fields

    def __setattr__(self, key: str, value: t.Any) -> t.NoReturn:
        if self._fields is not None and key in self._fields:
            field_class: ModelField = self._fields[key]
            field_class.value = value
            self._fields[key] = field_class
        elif key.startswith("_"):
            super().__setattr__(key, value)
        else:
            raise MinosModelException(f"model attribute {key} doesn't exist")

    def __getattr__(self, item: str) -> t.Any:
        if self._fields is not None and item in self._fields:
            return self._fields[item].value
        else:
            raise AttributeError(f"{type(self).__name__!r} does not contain the {item!r} attribute.")

    # noinspection PyMethodParameters
    @self_or_classmethod
    @abstractmethod
    def _type_hints(self_or_cls) -> dict[str, t.Any]:
        pass

    # noinspection PyMethodParameters
    @property_or_classproperty
    def avro_schema(self_or_cls) -> list[dict[str, t.Any]]:
        """Compute the avro schema of the model.

        :return: A dictionary object.
        """

        fields = [
            AvroSchemaEncoder(field_name, field_type).build() for field_name, field_type in self_or_cls._type_hints()
        ]
        schema = {
            "name": self_or_cls._avro_name,
            "type": "record",
            "fields": fields,
        }
        if self_or_cls._avro_namespace is not None:
            schema["namespace"] = self_or_cls._avro_namespace

        return [schema]

    # noinspection PyMethodParameters
    @classproperty
    def _avro_name(cls) -> str:
        return cls.__name__

    # noinspection PyMethodParameters
    @classproperty
    def _avro_namespace(cls) -> t.Optional[str]:
        return cls.__module__

    @property
    def avro_data(self) -> dict[str, t.Any]:
        """Compute the avro data of the model.

        :return: A dictionary object.
        """
        return {name: field.avro_data for name, field in self.fields.items()}

    @property
    def avro_str(self) -> str:
        """Generate bytes representation of the current instance.

        :return: A bytes object.
        """
        # noinspection PyTypeChecker
        return b64encode(self.avro_bytes).decode()

    @property
    def avro_bytes(self) -> bytes:
        """Generate bytes representation of the current instance.

        :return: A bytes object.
        """
        # noinspection PyTypeChecker
        return MinosAvroProtocol().encode(self.avro_data, self.avro_schema)

    def __eq__(self, other: T) -> bool:
        return type(self) == type(other) and self.fields == other.fields

    def __hash__(self) -> int:
        return hash(tuple(self))

    def __iter__(self) -> t.Iterable:
        # noinspection PyRedundantParentheses
        yield from self.fields.items()

    def __repr__(self):
        fields_repr = ", ".join(repr(field) for field in self.fields.values())
        return f"{type(self).__name__}(fields=[{fields_repr}])"
