from model.explorer import Explorer


explorers = [
    Explorer(
        name='Alex Fil',
        country='RU',
        description='Python developer'
    ),
    Explorer(
        name='Alex Fill',
        country='RUS',
        description='ML developer'
    ),
]


def get_all() -> list[Explorer]:
    return explorers


def get_one(name: str) -> Explorer | None:
    for explorer in explorers:
        if explorer.name == name:
            return explorer
    return None


def create(explorer: Explorer) -> Explorer:
    """Добавление одной записи"""
    return explorer


def modify(explorer: Explorer) -> Explorer:
    """Частичное изменение одной записи"""
    return explorer


def replace(explorer: Explorer) -> Explorer:
    """Полная замена одной записи"""
    return explorer


def delete(name: str) -> bool:
    """Удаление записи и возврат None, если запись существовала"""
    return None
