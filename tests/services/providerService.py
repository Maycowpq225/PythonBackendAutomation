from utils.settings import settings
import requests
from utils.createUserData import CreateUserData

baseUrl = settings["PROVIDER_URL"]

def createUser():
    userData = CreateUserData().to_json()
    response = requests.request("POST", f'{baseUrl}/register', json=userData)
    return response.json()