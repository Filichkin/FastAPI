from fastapi import FastAPI, Depends, params


app = FastAPI()


def user_dep(name: str = params, password: str = params):
    """Функция зависимости."""
    return {'name': name, 'valid': True}


@app.get('/user')
def get_user(user: dict = Depends(user_dep)) -> dict:
    """Функция пути/ Эндпоинт приложения."""
    return user
