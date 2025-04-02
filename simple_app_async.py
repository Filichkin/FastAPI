import asyncio
from fastapi import FastAPI
import uvicorn


app = FastAPI()


@app.get('/simple_app')
async def main():
    await asyncio.sleep(5)
    return 'Test FastAPI'


if __name__ == '__main__':
    uvicorn.run('simple_app_async:app')
