from fastapi import APIRouter
from .models import LoginSchema

router = APIRouter()

@router.post('/login')
async def login(data: LoginSchema):
    '''
    Route for users logging into their accounts
    '''

    message = ''

    status = 200 

    jwt_token = ''
    
    return {'message': message, 'status': status, 'jwt_token' : jwt_token}

