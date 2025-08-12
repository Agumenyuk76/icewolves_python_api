import requests

from pydantic_schemas.news_schemas import GetNewsSchema
from wsgiref import headers
from pydantic import BaseModel
from typing import List
from pydantic.v1.schema import schema

#СХЕМЫ_СХЕМЫ_СХЕМЫ_СХЕМЫ_СХЕМЫ_СХЕМЫ_СХЕМЫ_СХЕМЫ_СХЕМЫ_СХЕМЫ_СХЕМЫ_СХЕМЫ_СХЕМЫ_
class Rival(BaseModel): #соперники
    id: int
    logoImgLink: str
    name: str

class ListUsers(BaseModel):
    fullName: str
    id: int
    isParticipates: bool

class ListMatches(BaseModel):# список совпадений
    arena: str
    dateMatch: str
    id: int
    rival1: Rival
    rival1Score: str
    rival2: Rival
    rival2Score: str
    status: str
    type: str

class MatchesPostSchema(BaseModel):
    match: ListMatches #ОДИН МАТЧ!!!!

class MatchGetSchema(BaseModel):
    listMatches: List[ListMatches] #СПИСОК МАТЧЕЙ В ОБЕРТКЕ!!!!

class MatchGetLastSchema(BaseModel):
    listLastMatches: List[ListMatches] #писок списков, где каждый вложенный список содержит объекты типа ListMatches

class ListMatchById(BaseModel):
    arena: str
    dateMatch: str
    id: int
    isFinished: bool
    listUsers: List[ListUsers]
    rival1: Rival
    rival1Score: str
    rival2: Rival
    rival2Score: str
    status: str
    type: str

class MatchGetByIdSchema(BaseModel):
    match: ListMatchById
#СХЕМЫ_СХЕМЫ_СХЕМЫ_СХЕМЫ_СХЕМЫ_СХЕМЫ_СХЕМЫ_СХЕМЫ_СХЕМЫ_СХЕМЫ_СХЕМЫ_СХЕМЫ_СХЕМЫ_

def test_get_near_match (auth): #РАБОТАЕТ
    auth_token = None
    auth_token = auth
    print(auth_token)
    assert auth_token is not None, "Сначала необходимо выполнить авторизацию (test_user_authorization)"
    headers = {
        "Authorization": f"Bearer {auth_token}",
        "Content-Type": "application/json"
    }
    response = requests.get(
        url=f"https://icewolves-back.strongteam.pro/api/matches",
        headers=headers
    )

    assert response.status_code in [200, 201], (
        f"Ошибка создания новости. Код: {response.status_code}, "
        f"Ответ: {response.text}"
    )
    list_match = response.json()
    MatchGetSchema(**list_match)

    print(MatchGetSchema(**list_match))

def test_add_match (auth): #ГОТОВ, но падает на статус коде ==500, через постман также
    auth_token = None
    auth_token = auth
    print(auth_token)
    assert auth_token is not None, "Сначала необходимо выполнить авторизацию (test_user_authorization)"
    headers = {
        "Authorization": f"Bearer {auth_token}",
        "Content-Type": "application/json"
    }
    test_match = {
        "arenaId": 7,
        "dateMatch": "2024-11-23T18:15",
        "matchStatusId": 7,
        "matchTypesId": 7,
        "rival1Id": 7,
        "rival1Score": "7",
        "rival2Id": 7,
        "rival2Score": "7"
    }
    response = requests.post(
        url=f"https://icewolves-back.strongteam.pro/api/matches",
        json=test_match,
        headers=headers
    )
    assert response.status_code in [200, 201], (
        f"Ошибка создания матча. Код: {response.status_code}, "
        f"Ответ: {response.text}"
    )
    news_item = response.json()
    print(news_item)
    assert news_item["arenaId"] == test_match["arenaId"], "Не соответвует ID арены"
    assert news_item["dateMatch"] == test_match["dateMatch"], "Дата матча не совпадает"
    assert news_item["matchStatusId"] == test_match["matchStatusId"], "Статус матча не совпадает"
    assert news_item["matchTypesId"] == test_match["matchTypesId"], "Тип матча не совпадает"
    assert len(news_item["rival1Id"]) == len(test_match["rival1Id"]), "ID соперника 1 не совпадает"
    assert news_item["rival1Score"] == test_match["rival1Score"], "Оценка соперника 1 не совпадает"
    assert news_item["rival2Id"] == test_match["rival2Id"], "ID соперника 2 не совпадает"
    assert news_item["rival2Score"] == test_match["rival2Score"], "Оценка соперника 2 не совпадает"

    return news_item

def test_get_all_match_user (admin): #РАБОТАЕТ+ авторизация админа
    # почему ссылаемся на эту схему, а не на схему ListMatchById т.к. в ней есть поле isFinished
    admin_token = None
    admin_token = admin
    print(admin_token)
    assert admin_token is not None, "Сначала необходимо выполнить авторизацию (test_user_authorization)"
    headers = {
        "Authorization": f"Bearer {admin_token}",
        "Content-Type": "application/json"
    }
    response = requests.get(
        url=f"https://icewolves-back.strongteam.pro/api/matches/all",
        headers=headers
    )

    assert response.status_code in [200, 201], (
        f"Ошибка создания новости. Код: {response.status_code}, "
        f"Ответ: {response.text}"
    )
    list_match = response.json()
    MatchGetSchema(**list_match)

    print(MatchGetSchema(**list_match))


def test_add_player_match (admin): #АДМИН!!!
    # хотела добавить тест на проверку добавленного участника, но слишком мало данных-не могу его найти
    #попатка найтиигрока по id тоже провалилась т.к. ответ shemas..."players": []
    #падает 500
    # в посмане КОНФЛИКТ Эта вкладка Добавить игрока в комплект матча была изменена с другой вкладки. Сохранение этих изменений приведет к перезаписи запроса.
    admin_token = None
    admin_token = admin
    print(admin_token)
    assert admin_token is not None, "Сначала необходимо выполнить авторизацию (test_user_authorization)"
    headers = {
        "Authorization": f"Bearer {admin_token}",
        "Content-Type": "application/json"
    }
    test_player = {
  "matchId": 7,
  "userId": 7
    }
    response = requests.post(
        url=f"https://icewolves-back.strongteam.pro/api/matches/registration",
        json=test_player,
        headers=headers
    )
    assert response.status_code in [200, 201], (
        f"Ошибка создания матча. Код: {response.status_code}, "
        f"Ответ: {response.text}"
    )
    #assert response.json() # нужно написать проверку на текст сообщения "message": "OK"
    news_item = response.json()
    assert news_item["message"] == "OK", "Переделывай"
    print(response.json())

def test_delete_player_match (admin): # не работает, у никиты не описан
    #напрягает что этот запрос идентичен предыдущему, кроме метода
    admin_token = None
    admin_token = admin
    print(admin_token)
    assert admin_token is not None, "Сначала необходимо выполнить авторизацию (test_user_authorization)"
    headers = {
        "Authorization": f"Bearer {admin_token}",
        "Content-Type": "application/json"
    }
    test_player = {
  "matchId": 7,
  "userId": 7
    }
    response = requests.put(
        url=f"https://icewolves-back.strongteam.pro/api/matches/registration",
        json=test_player,
        headers=headers
    )
    assert response.status_code in [200, 201], (
        f"Ошибка создания матча. Код: {response.status_code}, "
        f"Ответ: {response.text}"
    )
    news_item = response.json()
    assert news_item["message"] == "OK", "Переделывай"
    print(response.json())

def test_delete_match(auth):  # 404
    auth_token = None
    auth_token = auth
    print(auth_token)
    assert auth_token is not None, "Сначала необходимо выполнить авторизацию (test_user_authorization)"
    headers = {
        "Authorization": f"Bearer {auth_token}",
        "Content-Type": "application/json"
    }
    response = requests.delete(
        url=f"https://icewolves-back.strongteam.pro//api/matches/7",# id команды можно поставить 261-уже существующий, но тк не мной создан дергать страшнно
        #не дает создать матч
        headers=headers
    )

    assert response.status_code in [200, 201], (
        f"Ошибка создания новости. Код: {response.status_code}, "
        f"Ответ: {response.text}"
    )
    news_item = response.json()
    assert news_item["message"] == "OK", "Переделывай"
    print(response.json())

def test_patch_match (admin): #АДМИН!!!
    admin_token = None
    admin_token = admin
    print(admin_token)
    assert admin_token is not None, "Сначала необходимо выполнить авторизацию (test_user_authorization)"
    headers = {
        "Authorization": f"Bearer {admin_token}",
        "Content-Type": "application/json"
    }
    test_match = {
  "arenaId": 1,
  "dateMatch": "2024-11-23T18:15",
  "matchStatusId": 1,
  "matchTypesId": 1,
  "rival1Id": 1,
  "rival1Score": "0",
  "rival2Id": 1,
  "rival2Score": "0"
}
    response = requests.patch(
        url=f"https://icewolves-back.strongteam.pro/api/matches/{id}",#261 можно изменить а потом его удалить
        json=test_match,
        headers=headers
    )
    assert response.status_code in [200, 201], (
        f"Ошибка создания матча. Код: {response.status_code}, "
        f"Ответ: {response.text}"
    )

    news_item = response.json()
    assert news_item["message"] == "OK", "Переделывай"
    print(response.json())

def test_get_match_id (admin): #АДМИН!!!
    admin_token = None
    admin_token = admin
    print(admin_token)
    assert admin_token is not None, "Сначала необходимо выполнить авторизацию (test_user_authorization)"
    headers = {
        "Authorization": f"Bearer {admin_token}",
        "Content-Type": "application/json"
    }

    response = requests.patch(
        url=f"https://icewolves-back.strongteam.pro/api/matches/261",#261 можно изменить а потом его удалить
        headers=headers
    )
    assert response.status_code in [200, 201], (
        f"Ошибка создания матча. Код: {response.status_code}, "
        f"Ответ: {response.text}"
    )
    news_item = response.json()
    print(news_item)
    assert news_item["Id"] == #как передать проверку id из запроса? url["Id"], "Не соответвует ID матча"