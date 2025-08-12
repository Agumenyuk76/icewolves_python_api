import pytest
import requests

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