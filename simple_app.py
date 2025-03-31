from fastapi import FastAPI
from fastapi import Response


app = FastAPI()


@app.get('/simple_app')
def greet(target):
    return f'Test FastAPI for {target}'


@app.get('/status')
def status(status_code=200):
    return 'success'


@app.get('/header/{name}/{value}')
def header(name: str, value: str, response: Response):
    response.headers[name] = value
    return 'normal_test'


if __name__ == '__main__':
    import uvicorn
    uvicorn.run('simple_app:app', reload=True)
