from wsgiref import headers

import pytest
import requests
import pytest
from typing import List
from pydantic import BaseModel, HttpUrl
from datetime import datetime

from pydantic_schemas import news_schemas


@pytest.fixture()
def auth():
    BASE_URL = "https://icewolves-back.strongteam.pro/api/"
    AUTH_ENDPOINT = "/auth/login"
    test_credentials = {
    "email": "iozeryakov@strongteam.tech",
    "password": "Password"
}
    response = requests.post(
        url=f"https://icewolves-back.strongteam.pro/api/auth/login",
        json=test_credentials,
        headers={"Content-Type": "application/json"}
    )
    assert response.status_code == 200, f"Ожидался код 200, получен {response.status_code}"
    response_data = response.json()
    token = response_data.get('accessToken')

    return token

@pytest.fixture()
def add_news(auth):
    global AUTH_TOKEN
    AUTH_TOKEN = auth
    print(AUTH_TOKEN)
    assert AUTH_TOKEN is not None, "Сначала необходимо выполнить авторизацию (test_user_authorization)"
    headers = {
        "Authorization": f"Bearer {AUTH_TOKEN}",
        "Content-Type": "application/json"
    }
    test_news = {
      "message": "Новость1",
      "photo": "https://google.com/hui.png",
      "photos": [
        "https://goodpics.cn/h.png",
        "https://goodpics.cn/h2.png"
      ],
      "title": "Новость1"
    }
    create_response = requests.post(
        url=f"https://icewolves-back.strongteam.pro/api/news",
        json=test_news,
        headers=headers
    )

    assert create_response.status_code in [200, 201], (
        f"Ошибка создания новости. Код: {create_response.status_code}, "
        f"Ответ: {create_response.text}"
    )

    news_item = create_response.json()

@pytest.fixture()
def admin():
    BASE_URL = "https://icewolves-back.strongteam.pro/api/"
    AUTH_ENDPOINT = "/auth/login"
    test_credentials = {
    "email": "vsmirnov@strongteam.tech",
    "password": "Qwerty1234"
}
    response = requests.post(
        url=f"https://icewolves-back.strongteam.pro/api/auth/login",
        json=test_credentials,
        headers={"Content-Type": "application/json"}
    )
    assert response.status_code == 200, f"Ожидался код 200, получен {response.status_code}"
    response_data = response.json()
    token = response_data.get('accessToken')

    return token