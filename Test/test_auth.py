import pytest
import requests

def test_user_authorization(auth):
    assert auth == 200, f"Ожидался код 200, получен {auth.status_code}"
    response_data = auth.json()
    print(f"\nТокен получен: {auth}")