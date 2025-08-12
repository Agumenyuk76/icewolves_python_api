from wsgiref import headers
import requests
from pydantic import BaseModel
from typing import List

from pydantic.v1.schema import schema

import pydantic_schemas.validator
# from api_testing_test.news.schemas import GetNewsSchema, NewsList
from pydantic_schemas.news_schemas import GetNewsSchema

def test_get_new (auth):
    global AUTH_TOKEN
    AUTH_TOKEN = auth
    print(AUTH_TOKEN)
    assert AUTH_TOKEN is not None, "Сначала необходимо выполнить авторизацию (test_user_authorization)"
    headers = {
        "Authorization": f"Bearer {AUTH_TOKEN}",
        "Content-Type": "application/json"
    }
    response = requests.get(
        url=f"https://icewolves-back.strongteam.pro/api/news",
        headers=headers
    )

    assert response.status_code in [200, 201], (
        f"Ошибка создания новости. Код: {response.status_code}, "
        f"Ответ: {response.text}"
    )

    news_list = response.json()
    # pydantic_schemas.validator.validator(GetNewsSchema, news_list)
    GetNewsSchema(**news_list)
    print(GetNewsSchema(**news_list))

# try:
#         validated_response = GetNewsSchema.parse_obj(response.json())
#     except Exception as e:
#         pytest.fail(f"Ответ не соответствует схеме GetNewsSchema. Ошибка: {e}")
# news_list = validated_response.news
# assert isinstance(news_list, list), "Поле news должно быть списком"
# if news_list:  # если хотим проверить только при непустом списке
#         first_news = news_list[0]
#         assert first_news.title, "Заголовок новости не должен быть пустым"
#         assert first_news.added_at, "Дата добавления должна быть указана"
# return news_list




def test_add_new (auth):
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
    print(news_item)
    assert news_item["message"] == "OK1", "Заголовок не совпадает"
    assert news_item["title"] == test_news["title"], "Заголовок не совпадает"
    assert news_item["message"] == test_news["message"], "Сообщение не совпадает"
    assert news_item["photo"] == test_news["photo"], "Фото не совпадает"
    assert len(news_item["photos"]) == len(test_news["photos"]), "Количество фото не совпадает"

    return news_item  # Возвращаем созданную новость для использования в других тестах