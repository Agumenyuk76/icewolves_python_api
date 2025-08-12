import pytest
import requests
import time

AUTH_TOKEN = None


# class Authorization:
#     token: str
#     expires_in: int
def test_user_authorization():
   global AUTH_TOKEN
   # BASE_URL = "https://icewolves-back.strongteam.pro/api/"
   # AUTH_ENDPOINT = "/auth/login"
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


# def test_get_alls_arenas(test_user_authorization):
#    global AUTH_TOKEN
#    assert AUTH_TOKEN is not None, "Сначала необходимо выполнить авторизацию (test_user_authorization)"
#    headers = {
#        "Authorization": f"Bearer {AUTH_TOKEN}",
#        "Content-Type": "application/json"
#    }
#    response = requests.get(
#        url=f"https://icewolves-back.strongteam.pro/api/arenas",
#        headers={"Content-Type": "application/json"}
#    )
#    assert response.status_code == 200, f"Ожидался код 200, получен {response.status_code}"
#    arenas_data = response.json()
#    print("\nПолученные данные об аренах:")
#    print(f"Всего арен: {len(arenas_data)}")
def test_add_arenas():
   global AUTH_TOKEN
   assert AUTH_TOKEN is not None, "Сначала необходимо выполнить авторизацию (test_user_authorization)"
   headers = {
       "Authorization": f"Bearer {AUTH_TOKEN}",
       "Content-Type": "application/json"
   }
   test_arena_name = {
       "name": "Чипусик"
   }
   response = requests.post(
       url=f"https://icewolves-back.strongteam.pro/api/arenas",
       json=test_arena_name,
       headers={"Content-Type": "application/json"}
   )
   assert response.status_code == 200, f"Ожидался код 200, получен {response.status_code}"
