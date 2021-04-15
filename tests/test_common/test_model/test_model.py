"""
Copyright (C) 2021 Clariteia SL

This file is part of minos framework.

Minos framework can not be copied and/or distributed without the express permission of Clariteia SL.
"""

from typing import Optional

import pytest

from minos.common import (
    MinosModelException,
    ModelField,
    MinosReqAttributeException,
    MinosTypeAttributeException,
    MinosMalformedAttributeException,
)
from tests.modelClasses import Customer, CustomerFailList, CustomerFailDict, ShoppingList, User, Analytics

import unittest


class TestMinosModel(unittest.TestCase):

    def test_constructor_args(self):
        model = Customer(1234, "johndoe", "John", "Doe")
        self.assertEqual(1234, model.id)
        self.assertEqual("johndoe", model.username)
        self.assertEqual("John", model.name)
        self.assertEqual("Doe", model.surname)

    def test_constructor_multiple_values(self):
        with self.assertRaises(TypeError):
            Customer(1234, id=1234)
        with self.assertRaises(TypeError):
            Customer(None, id=1234)

    def test_constructor_kwargs(self):
        model = Customer(id=1234, username="johndoe", name="John", surname="Doe")
        self.assertEqual(1234, model.id)
        self.assertEqual("johndoe", model.username)
        self.assertEqual("Doe", model.surname)
        self.assertEqual("John", model.name)

    def test_aggregate_setter(self):
        model = Customer(1234)
        model.name = "John"
        model.surname = "Doe"
        self.assertEqual(1234, model.id)
        self.assertEqual("Doe", model.surname)
        self.assertEqual("John", model.name)

    def test_aggregate_int_as_string_type_setter(self):
        model = Customer("1234")
        model.name = "John"
        self.assertEqual(1234, model.id)
        self.assertEqual("John", model.name)

    def test_aggregate_wrong_int_type_setter(self):
        with pytest.raises(MinosTypeAttributeException):
            Customer("1234S")

    def test_aggregate_string_type_setter(self):
        model = Customer(123)
        model.name = "John"
        self.assertEqual("John", model.name)

    def test_aggregate_wrong_string_type_setter(self):
        model = Customer(123)
        with pytest.raises(MinosTypeAttributeException):
            model.name = 456

    def test_aggregate_bool_type_setter(self):
        model = Customer(123)
        model.name = "John"
        model.is_admin = True
        self.assertTrue(model.is_admin)

    def test_aggregate_wrong_bool_type_setter(self):
        model = Customer(123)
        model.name = "John"
        with pytest.raises(MinosTypeAttributeException):
            model.is_admin = "True"

    def test_aggregate_empty_mandatory_field(self):
        with pytest.raises(MinosReqAttributeException):
            Customer()

    def test_model_is_freezed_class(self):
        model = Customer(123)
        with pytest.raises(MinosModelException):
            model.address = "str kennedy"

    def test_model_list_class_attribute(self):
        model = Customer(123)
        model.lists = [1, 5, 8, 6]

        self.assertEqual([1, 5, 8, 6], model.lists)

    def test_model_list_wrong_attribute_type(self):
        model = Customer(123)
        with pytest.raises(MinosTypeAttributeException):
            model.lists = [1, "hola", 8, 6]

    def test_model_ref(self):
        shopping_list = ShoppingList()
        user = User(1234)
        shopping_list.user = user
        self.assertEqual(user, shopping_list.user)

    def test_model_ref_raises(self):
        shopping_list = ShoppingList()
        with self.assertRaises(MinosTypeAttributeException):
            shopping_list.user = "foo"

    def test_recursive_type_composition(self):
        orders = {
            User(1): [ShoppingList(User(1)), ShoppingList(User(1))],
            User(2): [ShoppingList(User(2)), ShoppingList(User(2))]
        }

        analytics = Analytics(1, orders)
        self.assertEqual(orders, analytics.orders)

    def test_model_fail_list_class_attribute(self):
        with pytest.raises(MinosMalformedAttributeException):
            CustomerFailList(123)

    def test_model_fail_dict_class_attribute(self):
        with pytest.raises(MinosMalformedAttributeException):
            CustomerFailDict(123)

    def test_empty_required_value(self):
        with self.assertRaises(MinosReqAttributeException):
            User()

    def test_fields(self):
        fields = {
            'id': ModelField("id", int, 123), 'username': ModelField("username", Optional[str])
        }
        model = User(123)
        self.assertEqual(fields, model.fields)

    def test_equal(self):
        a, b = User(123), User(123)
        self.assertEqual(a, b)

    def test_not_equal(self):
        a, b = User(123), User(456)
        self.assertNotEqual(a, b)

    def test_iter(self):
        user = User(123)
        expected = {
            'id': ModelField("id", int, 123),
            'username': ModelField("username", Optional[str])
        }
        self.assertEqual(expected, dict(user))

    def test_hash(self):
        user = User(123)

        expected = hash(
            (
                ('id', ModelField("id", int, 123)),
                ('username', ModelField("username", Optional[str])),
            )
        )
        self.assertEqual(expected, hash(user))


if __name__ == '__main__':
    unittest.main()
