from fastapi import FastAPI, Depends, params


app = FastAPI()


def user_dep(name: str = params, password: str = params):
    """Функция зависимости."""
    return {'name': name, 'valid': True}


@app.get('/user')
def get_user(user: dict = Depends(user_dep)) -> dict:
    """Функция пути/ Эндпоинт приложения."""
    return user


def check_dep(name: str = params, password: str = params):
    if not name:
        raise


@app.get('/check_user', dependencies=[Depends[check_dep]])
def check_user() -> bool:
    return True
