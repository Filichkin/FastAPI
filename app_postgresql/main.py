from fastapi import FastAPI


app = FastAPI()


@app.get('/api/healthchecker')
def root():
    return {'message': 'Test of the endpoint'}


if __name__ == '__main__':
    import uvicorn
    uvicorn.run('main:app', reload=True)
