def test_authorization_and_create_arena():
    """Объединённый тест: авторизация + создание арены"""
    global AUTH_TOKEN

    # 1. Авторизация
    test_credentials = {
        "email": "iozeryakov@strongteam.tech",
        "password": "Password"
    }

    auth_response = requests.post(
        url="https://icewolves-back.strongteam.pro/api/auth/login",
        json=test_credentials,
        headers={"Content-Type": "application/json"}
    )

    assert auth_response.status_code == 200
    AUTH_TOKEN = auth_response.json().get('accessToken')
    assert AUTH_TOKEN is not None

    # 2. Создание арены
    headers = {
        "Authorization": f"Bearer {AUTH_TOKEN}",
        "Content-Type": "application/json"
    }

    test_arena = {
        "name": f"Арена_{int(time.time())}",
        "address": "ул. Тестовая, 1",
        "capacity": 5000
    }

    create_response = requests.post(
        url="https://icewolves-back.strongteam.pro/api/arenas",
        json=test_arena,
        headers=headers
    )

    assert create_response.status_code in [200, 201]
    print("\nСоздана арена:", create_response.json())