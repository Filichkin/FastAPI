from error import Duplicate, Missing
from .init import curs, conn, IntegrityError
from model.creature import Creature


curs.execute(
    """CREATE TABLE IF NOT EXISTS creature(
       name TEXT PRIMARY KEY,
       country TEXT,
       area TEXT,
       description TEXT,
       aka TEXT)"""
)


def row_to_model(row: tuple) -> Creature:
    name, description, country, area, aka = row
    return Creature(
        name=name,
        country=country,
        area=area,
        description=description,
        aka=aka
    )


def model_to_dict(creature: Creature) -> dict:
    return creature.dict()


def get_one(name: str) -> Creature:
    qry = 'SELECT * FROM creature WHERE name=:name'
    params = {'name': name}
    curs.execute(qry, params)
    row = curs.fetchone()
    if row:
        return row_to_model(row)
    else:
        raise Missing(msg=f'Creature {name} not found')


def get_all(name: str) -> list[Creature]:
    qry = 'SELECT * FROM creature'
    curs.execute(qry)
    rows = list(curs.fetchall())
    return [row_to_model(row) for row in rows]


def create(creature: Creature) -> Creature:
    qry = '''INSERT INTO creature VALUES
          (:name, :description, :country, :area, :aka)'''
    params = model_to_dict(creature)
    try:
        curs.execute(qry, params)
    except IntegrityError:
        raise Duplicate(
            msg=f'Creature {creature.name} already exists'
        )
    conn.commit()
    return get_one(creature.name)


def modify(name: str, creature: Creature) -> Creature:
    qry = '''UPDATE creature SET
             name=:name,
             country=:country,
             area=:area,
             description=:description,
             aka=:aka
             where name=:orig_name'''
    params = model_to_dict(creature)
    params['orig_name'] = name
    curs.execute(qry, params)
    if curs.rowcount == 1:
        conn.commit()
        return get_one(creature.name)
    else:
        raise Missing(msg=f'Creature {name} not found')


def delete(creature: Creature) -> bool:
    qry = 'DELETE FROM creature WHERE name=:name'
    params = {'name': creature.name}
    curs.execute(qry, params)
    conn.commit()
    if curs.rowcount != 1:
        raise Missing(msg=f'Creature {creature.name} not found')
