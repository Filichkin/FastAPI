from fastapi import FastAPI

from model import Creation


app = FastAPI()


@app.get('/creation')
def get_all() -> list[Creation]:
    from data import get_creations
    return get_creations()
