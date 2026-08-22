from collections import namedtuple
import requests
import pytest
from data.config import config
from users.users import test_user_1

Token = namedtuple("Token", ["token", "stand", "headers"])

@pytest.fixture(scope="session")
def access_token():
    stand = config.get("stand")
    body = {"email": test_user_1.get("login"),"password": test_user_1.get("password"),"isRememberMe":True}
    token = requests.post(f"{stand}/api/v1/auth/login", json=body).json()["token"]
    headers = {"Content-Type": "application/json", "Authorization": token}
    yield Token(token, stand, headers)

@pytest.fixture(scope="function")
def authorization_api(access_token,login,password):
    body = {"email": login,"password": password,"isRememberMe":True}
    response = requests.post(f"{access_token.stand}/api/v1/auth/login", json=body,headers=access_token.headers)
    return response

@pytest.fixture(scope="function")
def get_current_user_id(access_token):
    response = requests.get(f"{access_token.stand}/api/v1/user/current", headers=access_token.headers)
    return response.json()["userID"]

@pytest.fixture(scope="function")
def get_candidate(access_token,get_current_user_id):
    response = requests.get(f"{access_token.stand}/api/v1/user/candidate/{get_current_user_id}", headers=access_token.headers)
    return response.json()["content"][0]