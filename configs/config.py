import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    uri = os.getenv('URI')
    jwt_secret = os.getenv('JWT_SECRET')