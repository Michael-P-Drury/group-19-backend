from fastapi import APIRouter
from .models import LoginSchema, SignupSchema
import sqlite3
import jwt
import bcrypt
import os


router = APIRouter()

@router.post('/login')
async def login(data: LoginSchema):

    try:
        username = data.username
        password = data.password

        con = sqlite3.connect("group_19.db")
        cursor = con.cursor()

        query = 'SELECT password FROM users WHERE username = ?'
        res = cursor.execute(query, (username,))
        check_password = res.fetchone()

        con.commit()

        if check_password:

            check_password_string = check_password[0]

            password_bytes = password.encode('utf-8')
            check_password_bytes = check_password_string.encode('utf-8')

            matched_password = bcrypt.checkpw(password_bytes, check_password_bytes)

            if matched_password:
        
                status_message = 'Login Successful'
                status = 200 
                jwt_token = create_jwt_access_token({'sub': username})

            else:
                status_message = 'Incorrect password'
                status = 400
                jwt_token = None


        else:
            status_message = 'Error logging in user'
            status = 400
            jwt_token = None


    except Exception as e:
        status_message = f'Error logging in user: {e}'
        status = 400 
        jwt_token = None

    return {'status_message': status_message, 'status': status, 'jwt_token' : jwt_token}



@router.post('/signup')
async def signup(data: SignupSchema):

    try:
        username = data.username
        password = data.password

        con = sqlite3.connect("group_19.db")
        cursor = con.cursor()

        query = 'SELECT username FROM users WHERE username = ?'
        res = cursor.execute(query, (username,))
        found_username = res.fetchone()

        if not found_username:

            s = bcrypt.gensalt()
            password_bytes = password.encode('utf-8')
            hashed_password = bcrypt.hashpw(password_bytes, s)
            hashed_password_str = hashed_password.decode('utf-8')
            
            query = 'INSERT INTO users VALUES(?, ?)'

            cursor.execute(query, (username, hashed_password_str))
            con.commit()

            status_message = 'new account created successfully'
            status = 200

        else:
            status_message = 'User already exists'
            status = 400

    except Exception as e:
        status_message = f'Error creating new account: {e}'
        status = 400

    return {'status_message': status_message, 'status': status}




@router.post('/make_suggestion')
async def make_suggestion():
    pass




def create_jwt_access_token(data):

    to_encode = data.copy()

    secret_key = os.getenv('JWT_SECRET_KEY')
    algorithm = os.getenv('JWT_ALGORITHM')
    
    encoded_jwt = jwt.encode(to_encode, secret_key, algorithm=algorithm)
    return encoded_jwt