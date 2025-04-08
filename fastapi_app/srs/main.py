from fastapi import FastAPI
import uvicorn


app = FastAPI()


@app.get('/')
def top():
    return 'top here'


@app.get('/echo/{thing}')
def echo(thing):
    return f'echoing {thing}'


if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)
