# Смоделируем приложение для публикации своих текстов с подписочной системой:
# Ключевые классы:
# 1. Пользователь ()
# 2. Статья
# 3. Подписка

class Subscription:
    id: int
    name: str # название подписки
    description: str # описание подписки
    author_id: int # автор подписки
    amount: float # стоимость подписки
    type: str # тип подписки (ежегодная, ежемесечная, единоразовая и т.д.)
    is_archived: bool # заархивирована ли подписка (недоступна для покупки)




class User:
    id: int = 1
    nickname: str = 'username' # Никнейм пользователя
    subscriptions: list[int] = [] # Подписки пользователя
    description: str = 'chill' # Описание аккаунта
    
    def __init__(self, id, nickname, description):
        self.id = id
        self.nickname = nickname
        self.description = description
        self.subscriptions = []

    def subsribe(self, subscription):
        self.subscriptions.append(subscription)

    def change_nickname(self, new_nickname):
        self.nickname = new_nickname

    def change_description(self, new_description):
        self.description = new_description

    def print_user(self):
        print(f'### User: {self.id}')
        print(f'### Nickname: {self.nickname}')
        print(f'### Description: {self.description}')
        print(f'### Subscriptions: {self.subscriptions}')

class Article:
    id: int
    author_id: int # ИД автора статьи
    name: str # название статьи
    create_time: int # время создания статьи
    subscription_type: list[int] # Список ИД подписок, которым доступен этот материал
    text: str # Содержание статьи
    links: str # Ссылки на доп. материалы

