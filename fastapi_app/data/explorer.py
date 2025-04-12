from .init import curs

from model.explorer import Explorer


curs.execute(
    """CREATE TABLE IF NOT EXIST explorer(
       name PRIMARY KEY,
       country TEXT,
       description TEXT)"""
)


def row_to_model(row: tuple) -> Explorer:
    name, country, description = row
    return Explorer(name=name, country=country, description=description)


def model_to_dict(explorer: Explorer) -> dict:
    return explorer.dict()


def get_one(name: str) -> Explorer:
    qry = 'SELECT * FROM explorer WHERE name=:name'
    params = {'name': name}
    curs.execute(qry, params)
    row = curs.fetchone()
    return row_to_model(row)


def get_all() -> list[Explorer]:
    qry = 'SELECT * FROM explorer'
    curs.execute(qry)
    return [row_to_model(row) for row in curs.fetchall()]


def create(explorer: Explorer) -> Explorer:
    qry = '''INSERT INTO explorer
             (name, country, description) VALUES
             (:name, :country, :description)'''
    params = model_to_dict(explorer)
    _ = curs.execute(qry, params)
    return get_one(explorer.name)


def modify(name: str, explorer: Explorer) -> Explorer:
    qry = '''UPDATE explorer
             SET name=:name, country=:country,
                 description=:description
             WHERE name=:orig_name'''
    params = model_to_dict(explorer)
    params['orig_name'] = name
    _ = curs.execute(qry, params)
    return get_one(explorer.name)


def delete(name: str) -> bool:
    qry = 'DELETE FROM explorer WHERE name = :name'
    params = {'name': name}
    result = curs.execute(qry, params)
    return bool(result)
