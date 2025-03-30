from fastapi import FastAPI


app = FastAPI()


@app.get('/simple_app')
def greet():
    return 'Test FastAPI'


if __name__ == '__main__':
    import uvicorn
    uvicorn.run('simple_app:app', reload=True)
