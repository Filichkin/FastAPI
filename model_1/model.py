from pydantic import BaseModel


class Creation(BaseModel):
    name: str
    country: str
    area: str
    description: str
    slug: str


create = Creation(
    name='Alex',
    country='Russia',
    area='Moscow region',
    description='Python developer',
    slug='alex'

)

print('Name is', create.name)
