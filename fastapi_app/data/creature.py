from .init import curs

from model.creature import Creature


curs.execute(
    """CREATE TABLE IF NOT EXIST creature(
       name TEXT PRIMARY KEY,
       country TEXT,
       area TEXT,
       description TEXT,
       aka TEXT)"""
)


def row_to_model(row: tuple) -> Creature:
    name, description, country, area, aka = row
    return Creature(name, description, country, area, aka)


def model_to_dict(creature: Creature) -> dict:
    return creature.dict()


def get_one(name: str) -> Creature:
    qry = 'SELECT * FROM creature WHERE name=:name'
    params = {'name': name}
    curs.execute(qry, params)
    row = curs.fetchone()
    return row_to_model(row)


def get_all(name: str) -> list[Creature]:
    qry = 'SELECT * FROM creature'
    curs.execute(qry)
    rows = list(curs.fetchall())
    return [row_to_model(row) for row in rows]


def create(creature: Creature) -> Creature:
    qry = '''INSERT INTO creature VALUES
          (:name, :description, c:ountry, :area, :aka)'''
    params = model_to_dict(creature)
    curs.execute(qry, params)


def modify(creature: Creature) -> Creature:
    qry = '''UPDATE creature SET
             name=:name,
             country=:country,
             area=:area,
             description=:description,
             aka=:aka
             where name=:orig_name'''
    params = model_to_dict(creature)
    params['orig_name'] = creature.name
    _ = curs.execute(qry, params)
    return get_one(creature.name)


def delete(creature: Creature) -> bool:
    qry = 'DELETE FROM creature WHERE name=:name'
    params = {'name': creature.name}
    result = curs.execute(qry, params)
    return bool(result)
