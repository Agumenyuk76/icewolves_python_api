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
    listLastMatches: List[ListMatches] #список списков, где каждый вложенный список содержит объекты типа ListMatches
# а где используется "список списков"?

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
    # попробуй авторизацию админа. Возможно не правильно реализовали обработку ошибки, 500 вместо 401 или 403
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
    #попытка найти игрока по id тоже провалилась т.к. ответ shemas..."players": []
    #падает 500
    # запрос на получение ишроков из команды с id 1, предлагаю взять любого для теста
    # curl --request GET \
    #   --url https://icewolves-back.strongteam.pro/api/players/1 \
    #   --header 'Accept: application/json'

    # в посмане КОНФЛИКТ Эта вкладка Добавить игрока в комплект матча была изменена с другой вкладки. Сохранение этих изменений приведет к перезаписи запроса.
    # Предположу, что в постмане 2 раза открыта одна и таже вкладка, поэтому ругается. Надо выбрать одну правильную
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
    # хорошо, что напрягает реализация. для удаления существует метод DELETE, хорошо бы переделать разабам. Пропусти
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
    # обрати внимание на оступы при объявлении json-ов, можно накинуть отступов и будет хорошо, как сделала ниже
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
    # пробовала запустить тест без двух символов слэша ?
    response = requests.delete(
        url=f"https://icewolves-back.strongteam.pro//api/matches/7",# id команды можно поставить 261-уже существующий, но тк не мной создан дергать страшнно
        #не дает создать матч
        # а как ты методом delete планировала удалить матч?
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
        # используешь функционал f'string, который позволяет подставить значение через {}, помещаешь туда id.
        # А где объявляется id ? Чему он равен?
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
    # assert news_item["Id"] == #как передать проверку id из запроса? url["Id"], "Не соответвует ID матча"

    # Используешь метод patch, при этом не передаешь никакого тела запроса. Нет изменений или я не понял твою проверку.
    # Тут же вижу, что по спеке этот запрос в ответе получает только $schema и message. Если хочешь проверить,
    # что изменения применились к нужному ID, внеси в него изменения, а потом через получение проверь, что изменение применилось.
