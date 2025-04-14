from fastapi import Depends, FastAPI, HTTPException
from fastapi.security import HTTPBasic, HTTPBasicCredentials
import uvicorn


app = FastAPI()

secret_user: str = 'superuser'
secret_password: str = 'YEMZ2509'

basic: HTTPBasicCredentials = HTTPBasic()


@app.get('/user_auth')
def get_user(creds: HTTPBasicCredentials = Depends(basic)) -> dict:
    if (creds.username == secret_user and creds.password == secret_password):
        return {
            'username': creds.username,
            'password': creds.password
            }
    raise HTTPException(status_code=401, detail='Incorrect auth data')


if __name__ == '__main__':
    uvicorn.run('auth_user:app', reload=True)
