from utils.settings import settings
import requests
from utils.create_user_data import CreateUserData

baseUrl = settings["PROVIDER_URL"]

def create_user():
    user_data = CreateUserData().to_json()
    response = requests.request("POST", f'{baseUrl}/register', json=user_data)
    return response