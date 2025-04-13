from fastapi import APIRouter, HTTPException

import data.creature as service
from error import Duplicate, Missing
from model.creature import Creature


router = APIRouter(prefix='/creature')


@router.get('', status_code=201)
@router.get('/', status_code=201)
def get_all() -> list[Creature]:
    return service.get_all()


@router.get('/{name}')
def get_one(name) -> Creature:
    try:
        return service.get_one(name)
    except Missing as exc:
        raise HTTPException(status_code=404, detail=exc.msg)


@router.post('/')
def create(creature: Creature) -> Creature:
    try:
        return service.create(creature)
    except Duplicate as exc:
        raise HTTPException(status_code=404, detail=exc.msg)


@router.patch('/')
def modify(creature: Creature) -> Creature:
    try:
        return service.modify(creature)
    except Missing as exc:
        raise HTTPException(status_code=404, detail=exc.msg)


@router.put('/')
def replace(creature: Creature) -> Creature:
    return service.replace(creature)


@router.delete('/{name}', status_code=204)
def delete(name: str):
    try:
        return service.delete(name)
    except Missing as exc:
        raise HTTPException(status_code=404, detail=exc.msg)
