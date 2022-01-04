from __future__ import (
    annotations,
)

import logging
from contextlib import (
    suppress,
)
from datetime import (
    date,
    datetime,
    time,
    timedelta,
)
from typing import (
    Any,
    Union,
)
from uuid import (
    UUID,
)

from ...exceptions import (
    MinosImportException,
    MinosMalformedAttributeException,
)
from ...importlib import (
    import_module,
)
from ..types import (
    MissingSentinel,
    ModelType,
    NoneType,
    build_union,
    is_model_type,
)
from .constants import (
    AVRO_ARRAY,
    AVRO_BOOLEAN,
    AVRO_BYTES,
    AVRO_DATE,
    AVRO_DOUBLE,
    AVRO_FLOAT,
    AVRO_INT,
    AVRO_MAP,
    AVRO_NULL,
    AVRO_RECORD,
    AVRO_SET,
    AVRO_STRING,
    AVRO_TIME,
    AVRO_TIMEDELTA,
    AVRO_TIMESTAMP,
    AVRO_UUID,
)

logger = logging.getLogger(__name__)


class AvroSchemaDecoder:
    """Avro Schema Decoder class."""

    def __init__(self, schema: Any = None):
        self._schema = schema

    def build(self, schema: Any = MissingSentinel) -> type:
        """Build type from given avro schema item.

        :return: A dictionary object.
        """
        if schema is MissingSentinel:
            schema = self._schema
        return self._build(schema)

    def _build(self, schema: Union[ModelType, dict, list, str]) -> type:
        if isinstance(schema, ModelType):
            return schema

        if isinstance(schema, dict):
            return self._build_from_dict(schema)

        if isinstance(schema, list):
            return self._build_from_list(schema)

        return self._build_simple(schema)

    def _build_from_list(self, schema: list[Any]) -> type:
        options = tuple(self._build(entry) for entry in schema)
        return build_union(options)

    def _build_from_dict(self, schema: dict) -> type:
        if "logicalType" in schema:
            return self._build_logical_type(schema)

        if schema["type"] == AVRO_ARRAY:
            return self._build_list(schema)

        if schema["type"] == AVRO_MAP:
            return self._build_dict(schema)

        if schema["type"] == AVRO_RECORD:
            return self._build_record(schema)

        return self._build_type(schema)

    def _build_logical_type(self, schema: dict[str, Any]) -> type:
        logical_type = schema["logicalType"]
        if logical_type == AVRO_DATE["logicalType"]:
            return date

        if logical_type == AVRO_TIME["logicalType"]:
            return time

        if logical_type == AVRO_TIMESTAMP["logicalType"]:
            return datetime

        if logical_type == AVRO_TIMEDELTA["logicalType"]:
            return timedelta

        if logical_type == AVRO_UUID["logicalType"]:
            return UUID

        if logical_type == AVRO_SET["logicalType"]:
            return self._build_set(schema)

        with suppress(MinosImportException):
            type_ = import_module(logical_type)
            if not is_model_type(type_):
                return type_
            # noinspection PyUnresolvedReferences
            return type_.decode_schema(self, {k: v for k, v in schema.items() if k != "logicalType"})

        return self._build({k: v for k, v in schema.items() if k != "logicalType"})

    def _build_list(self, schema: dict[str, Any]) -> type:
        items = schema["items"]
        return list[self._build_iterable(items)]

    def _build_set(self, schema: dict[str, Any]) -> type:
        items = schema["items"]
        return set[self._build_iterable(items)]

    def _build_dict(self, schema: dict[str, Any]) -> type:
        values = schema["values"]
        return dict[str, self._build_iterable(values)]

    def _build_iterable(self, values: Union[dict, str, Any]) -> type:
        type_ = self._build(values)
        if type_ is NoneType:
            # FIXME: This is a design decision that must be revisited in the future.
            type_ = Any
        return type_

    def _build_record(self, schema: dict[str, Any]) -> type:
        type_ = ModelType.build(
            name_=schema["name"],
            type_hints_={field["name"]: self._build(field) for field in schema["fields"]},
            namespace_=schema.get("namespace"),
        )

        type_ = self._unpatch_namespace(type_)

        return type_.decode_schema(self, type_)

    @staticmethod
    def _unpatch_namespace(type_: ModelType) -> ModelType:
        type_.namespace = type_.namespace.rsplit(".", 1)[0]
        return type_

    def _build_type(self, schema: dict[str, Any]) -> type:
        return self._build(schema["type"])

    @staticmethod
    def _build_simple(type_: str) -> type:
        if type_ == AVRO_NULL:
            return NoneType

        if type_ == AVRO_INT:
            return int

        if type_ == AVRO_BOOLEAN:
            return bool

        if type_ == AVRO_FLOAT:
            return float

        if type_ == AVRO_DOUBLE:
            return float

        if type_ == AVRO_STRING:
            return str

        if type_ == AVRO_BYTES:
            return bytes

        raise MinosMalformedAttributeException(f"Given field type is not supported: {type_!r}")
