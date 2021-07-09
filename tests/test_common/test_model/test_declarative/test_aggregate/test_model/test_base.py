"""
Copyright (C) 2021 Clariteia SL

This file is part of minos framework.

Minos framework can not be copied and/or distributed without the express permission of Clariteia SL.
"""
import unittest
from uuid import (
    uuid4,
)

from minos.common import (
    NULL_UUID,
    InMemoryRepository,
    InMemorySnapshot,
    MinosRepositoryManuallySetAggregateIdentifierException,
    MinosRepositoryManuallySetAggregateVersionException,
    MinosSnapshotAggregateNotFoundException,
    MinosSnapshotDeletedAggregateException,
)
from tests.aggregate_classes import (
    Car,
)
from tests.utils import (
    FakeBroker,
)


class TestAggregate(unittest.IsolatedAsyncioTestCase):
    async def test_create(self):
        async with FakeBroker() as b, InMemoryRepository() as r, InMemorySnapshot() as s:
            observed = await Car.create(doors=3, color="blue", _broker=b, _repository=r, _snapshot=s)
            expected = Car(3, "blue", uuid=observed.uuid, version=1, _broker=b, _repository=r, _snapshot=s)
            self.assertEqual(expected, observed)

    async def test_create_raises(self):
        async with FakeBroker() as b, InMemoryRepository() as r, InMemorySnapshot() as s:
            with self.assertRaises(MinosRepositoryManuallySetAggregateIdentifierException):
                await Car.create(uuid=uuid4(), doors=3, color="blue", _broker=b, _repository=r, _snapshot=s)
            with self.assertRaises(MinosRepositoryManuallySetAggregateVersionException):
                await Car.create(version=1, doors=3, color="blue", _broker=b, _repository=r, _snapshot=s)

    async def test_classname(self):
        self.assertEqual("tests.aggregate_classes.Car", Car.classname)

    async def test_get(self):
        async with FakeBroker() as b, InMemoryRepository() as r, InMemorySnapshot() as s:
            originals = [
                await Car.create(doors=3, color="blue", _broker=b, _repository=r, _snapshot=s),
                await Car.create(doors=3, color="red", _broker=b, _repository=r, _snapshot=s),
                await Car.create(doors=5, color="blue", _broker=b, _repository=r, _snapshot=s),
            ]
            iterable = Car.get([o.uuid for o in originals], _broker=b, _repository=r, _snapshot=s)
            recovered = [v async for v in iterable]

            self.assertEqual(originals, recovered)

    async def test_get_one(self):
        async with FakeBroker() as b, InMemoryRepository() as r, InMemorySnapshot() as s:
            original = await Car.create(doors=3, color="blue", _broker=b, _repository=r, _snapshot=s)
            recovered = await Car.get_one(original.uuid, _broker=b, _repository=r, _snapshot=s)

            self.assertEqual(original, recovered)

    async def test_get_one_raises(self):
        async with FakeBroker() as b, InMemoryRepository() as r, InMemorySnapshot() as s:
            with self.assertRaises(MinosSnapshotAggregateNotFoundException):
                await Car.get_one(NULL_UUID, _broker=b, _repository=r, _snapshot=s)

    async def test_update(self):
        async with FakeBroker() as b, InMemoryRepository() as r, InMemorySnapshot() as s:
            car = await Car.create(doors=3, color="blue", _broker=b, _repository=r, _snapshot=s)

            await car.update(color="red")
            self.assertEqual(Car(3, "red", uuid=car.uuid, version=2, _broker=b, _repository=r, _snapshot=s), car)
            self.assertEqual(car, await Car.get_one(car.uuid, _broker=b, _repository=r, _snapshot=s))

            await car.update(doors=5)
            self.assertEqual(Car(5, "red", uuid=car.uuid, version=3, _broker=b, _repository=r, _snapshot=s), car)
            self.assertEqual(car, await Car.get_one(car.uuid, _broker=b, _repository=r, _snapshot=s))

    async def test_update_raises(self):
        async with FakeBroker() as b, InMemoryRepository() as r, InMemorySnapshot() as s:
            with self.assertRaises(MinosRepositoryManuallySetAggregateVersionException):
                await Car(3, "blue", id=1, version=1, _broker=b, _repository=r, _snapshot=s).update(version=1)

    async def test_refresh(self):
        async with FakeBroker() as b, InMemoryRepository() as r, InMemorySnapshot() as s:
            car = await Car.create(doors=3, color="blue", _broker=b, _repository=r, _snapshot=s)
            uuid = car.uuid

            car2 = await Car.get_one(uuid, _broker=b, _repository=r, _snapshot=s)
            await car2.update(color="red", _broker=b, _repository=r, _snapshot=s)
            await car2.update(doors=5, _broker=b, _repository=r, _snapshot=s)

            self.assertEqual(Car(3, "blue", uuid=uuid, version=1, _broker=b, _repository=r, _snapshot=s), car)
            await car.refresh()
            self.assertEqual(Car(5, "red", uuid=uuid, version=3, _broker=b, _repository=r, _snapshot=s), car)

    async def test_save_create(self):
        async with FakeBroker() as b, InMemoryRepository() as r, InMemorySnapshot() as s:
            car = Car(3, "blue", _broker=b, _repository=r, _snapshot=s)
            car.color = "red"
            car.doors = 5

            with self.assertRaises(MinosSnapshotAggregateNotFoundException):
                await car.refresh()

            await car.save()
            self.assertEqual(Car(5, "red", uuid=car.uuid, version=1, _broker=b, _repository=r, _snapshot=s), car)

    async def test_save_update(self):
        async with FakeBroker() as b, InMemoryRepository() as r, InMemorySnapshot() as s:
            car = await Car.create(doors=3, color="blue", _broker=b, _repository=r, _snapshot=s)

            uuid = car.uuid

            car.color = "red"
            car.doors = 5

            self.assertEqual(
                Car(3, "blue", uuid=uuid, version=1, _broker=b, _repository=r, _snapshot=s),
                await Car.get_one(uuid, _broker=b, _repository=r, _snapshot=s),
            )

            await car.save()
            self.assertEqual(Car(5, "red", uuid=uuid, version=2, _broker=b, _repository=r, _snapshot=s), car)
            self.assertEqual(
                Car(5, "red", uuid=uuid, version=2, _broker=b, _repository=r, _snapshot=s),
                await Car.get_one(uuid, _broker=b, _repository=r, _snapshot=s),
            )

    async def test_save_raises(self):
        async with FakeBroker() as b, InMemoryRepository() as r, InMemorySnapshot() as s:
            with self.assertRaises(MinosRepositoryManuallySetAggregateIdentifierException):
                await Car(3, "blue", uuid=uuid4(), _broker=b, _repository=r, _snapshot=s).save()
            with self.assertRaises(MinosRepositoryManuallySetAggregateVersionException):
                await Car(3, "blue", version=1, _broker=b, _repository=r, _snapshot=s).save()

    async def test_delete(self):
        async with FakeBroker() as b, InMemoryRepository() as r, InMemorySnapshot() as s:
            car = await Car.create(doors=3, color="blue", _broker=b, _repository=r, _snapshot=s)
            await car.delete()
            with self.assertRaises(MinosSnapshotDeletedAggregateException):
                await Car.get_one(car.uuid, _broker=b, _repository=r, _snapshot=s)


if __name__ == "__main__":
    unittest.main()
