from fastapi import APIRouter, HTTPException
from modules.database import SessionLocal
import lorem
from lorem.text import TextLorem
import names

router = APIRouter()

from uuid import uuid4
import random

from modules import utils



@router.get('/')
async def al_root():
    return utils.response({"message":"It seems you're looking for a friend"})

@router.get('/generate_password')
async def generate_password(length: int = 12):
    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+-'
    password = ''.join(random.choice(chars) for _ in range(length))
    return utils.response({"password":password})

@router.get('/generate_seed')
async def generate_seed(length: int = 24):
    chars = '0123456789'
    seed = ''.join(random.choice(chars) for _ in range(length))
    return utils.response({"seed":seed})

@router.get('/generate_uuid')
async def generate_uuid():
    return utils.response({"uuid":str(uuid4())})

@router.get('/generate_quote')
async def generate_quote(mode: str='paragraph'):
    match mode:
        case 'paragraph':
            text = lorem.paragraph()
        case 'text':    
            text = lorem.text()
        case 'sentence':
            text = lorem.sentence()
        case 'word':
            word_lorem = TextLorem(srange=(2,5))
            text = word_lorem.sentence()
        case _:
            raise HTTPException(status_code=400, detail='Invalid mode')
            
    return utils.response({"quote":text})

@router.get('/random_first_name')
async def randomFirstName():
    return utils.response({"first_name":names.get_first_name()})
    
@router.get('/random_last_name')
async def randomLastName():
    return utils.response({"last_name":names.get_last_name()})
    
@router.get('/root_directory')
async def get_root():
    return utils.response({"directory":utils.get_project_root()})
