from dataclasses import dataclass
import datetime

@dataclass
class User:
    username: str
    created_at: datetime.datetime
    birthday: datetime.datetime | None = None

def validate_user_on_server(_): pass

def validate_user(user: User):
    """ check user"""
    validate_user_on_server(user)
    print(user)

user = User('name', datetime.datetime(2025, 10, 10))
print(validate_user(user))
