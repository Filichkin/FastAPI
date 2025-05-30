from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from config import settings
from routers import user, auth, post


app = FastAPI()

origins = [
    settings.CLIENT_ORIGIN,
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

app.include_router(auth.router, tags=['Auth'], prefix='/api/auth')
app.include_router(user.router, tags=['Users'], prefix='/api/users')
app.include_router(post.router, tags=['Posts'], prefix='/api/posts')


@app.get('/api/healthchecker')
def root():
    return {'message': 'Test of the endpoint'}


if __name__ == '__main__':
    import uvicorn
    uvicorn.run('main:app', reload=True)
