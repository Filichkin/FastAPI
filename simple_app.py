from fastapi import FastAPI


app = FastAPI()


@app.get('/simple_app')
def greet(target):
    return f'Test FastAPI for {target}'


if __name__ == '__main__':
    import uvicorn
    uvicorn.run('simple_app:app', reload=True)
