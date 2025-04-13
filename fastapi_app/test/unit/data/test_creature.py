import os
import pytest

from model.creature import Creature
from error import Missing, Duplicate


os.environ['TEST_SQLITE_DB'] = ':memory:'
from data import creature


@pytest.fixture
def sample() -> Creature:
    return Creature(
        name='Dev',
        country='AU',
        area='Melburn',
        description='Spider tester',
        aka='Go'
        )


def test_create(sample):
    resp = creature.create(sample)
    assert resp == sample


def test_create_duplicate(sample):
    with pytest.raises(Duplicate):
        _ = creature.create(sample)


def test_get_one(sample):
    resp = creature.get_one(sample.name)
    assert resp == sample


def test_get_one_missing():
    with pytest.raises(Missing):
        _ = creature.get_one('FFF')


def test_modify(sample):
    creature.area = 'Sidney'
    resp = creature.modify(sample.name, sample)
    assert resp != sample


def test_modify_missing():
    thing: Creature = Creature(
        name='Dep',
        country='RU',
        area='',
        description='some thing',
        aka=''
    )
    with pytest.raises(Missing):
        _ = creature.modify(thing.name, thing)


def test_delete(sample):
    resp = creature.delete(sample)
    assert resp is None


def test_delete_missing(sample):
    with pytest.raises(Missing):
        _ = creature.delete(sample)
