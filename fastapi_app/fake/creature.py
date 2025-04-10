from model.creature import Creature


creatures = [
    Creature(
        name='Tester',
        country='AU',
        area='Melburn',
        description='Good traveler',
        aka='Python'
        ),
    Creature(
        name='Dev',
        country='KG',
        area='Bishkek',
        description='Good dev',
        aka='Java'
        ),
]


def get_all() -> list[Creature]:
    return creatures


def get_one(name: str) -> Creature | None:
    for creater in creatures:
        if creater.name == name:
            return creater
    return None


def create(creature: Creature) -> Creature:
    """Добавление одной записи"""
    return creature


def modify(creature: Creature) -> Creature:
    """Частичное изменение одной записи"""
    return creature


def replace(creature: Creature) -> Creature:
    """Полная замена одной записи"""
    return creature


def delete(name: str) -> bool:
    """Удаление записи и возврат None, если запись существовала"""
    return None
