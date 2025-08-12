import requests


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