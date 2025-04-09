from fastapi import FastAPI
import uvicorn

from web import explorer


app = FastAPI()

app.include_router(explorer.router)


@app.get('/')
def top():
    return 'top here'


@app.get('/echo/{thing}')
def echo(thing):
    return f'echoing {thing}'


if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)
