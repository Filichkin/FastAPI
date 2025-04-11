from model.creature import Creature
from service import creature as code


sample = Creature(
        name='Tester',
        country='AU',
        area='Melburn',
        description='Good traveler',
        aka='Python'
    )


def test_create():
    result = code.create(sample)
    assert result == sample


def test_get_exist():
    result = code.get_one('Tester')
    assert result == sample


def test_get_missing():
    result = code.get_one('Best')
    assert result is None
