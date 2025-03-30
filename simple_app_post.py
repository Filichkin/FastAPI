from fastapi import FastAPI, Body


app = FastAPI()


@app.post('/simple_app')
def greet(target: str = Body(embed=True)):
    return f'Test FastAPI for {target}'


if __name__ == '__main__':
    import uvicorn
    uvicorn.run('simple_app:app', reload=True)
