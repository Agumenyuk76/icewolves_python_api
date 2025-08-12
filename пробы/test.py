import pytest
import requests
import time

AUTH_TOKEN = None

# class Authorization:
#     token: str
#     expires_in: int
def test_user_authorization():
    global AUTH_TOKEN
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
AUTH_TOKEN = response_data.get('accessToken')

def test_get_alls_arenas():
    global AUTH_TOKEN
    assert AUTH_TOKEN is not None, "Сначала необходимо выполнить авторизацию (test_user_authorization)"
    headers = {
        "Authorization": f"Bearer {AUTH_TOKEN}",
        "Content-Type": "application/json"
    }
    response = requests.get(
        url=f"https://icewolves-back.strongteam.pro/api/arenas",
        headers={"Content-Type": "application/json"}
    )
    assert response.status_code == 200, f"Ожидался код 200, получен {response.status_code}"
    arenas_data = response.json()
    print("\nПолученные данные об аренах:")
    print(f"Всего арен: {len(arenas_data)}")

def test_add_and_verify_arena(auth):
    global AUTH_TOKEN
    AUTH_TOKEN = auth
    print(AUTH_TOKEN)
    assert AUTH_TOKEN is not None, "Сначала необходимо выполнить авторизацию (test_user_authorization)"
    headers = {
        "Authorization": f"Bearer {AUTH_TOKEN}",
        "Content-Type": "application/json"
    }
    test_arena = {
        "name": "Арена111"
    }
    create_response = requests.post(
        url=f"https://icewolves-back.strongteam.pro/api/arenas",
        json=test_arena,
        headers=headers
    )
    assert create_response.status_code in [200, 201], f"Ошибка создания: {create_response.status_code}"
    # created_arena = create_response.json()
    # arena_id = created_arena.get('id')
    # assert arena_id is not None, "В ответе отсутствует ID созданной арены"
    #
    # print(f"\nСоздана арена с ID: {arena_id}")