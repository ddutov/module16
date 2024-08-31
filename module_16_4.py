from typing import List
from fastapi import FastAPI, Body, HTTPException
from pydantic import BaseModel

app = FastAPI()
users = []


class User(BaseModel):
    id: int = None
    username: str
    age: int


@app.get('/users')
async def get_all_users() -> List[User]:
    return users


@app.post(path='/user/{username}/{age}')
async def create_user(user: User, username: str, age: int) -> User:
    user.id = int(list(users[-1].keys())[0]) + 1
    user.username = username
    user.age = age
    users.append(user)
    return user


@app.put('/user/{user_id}/{username}/{age}')
async def update_user(user_id: int, username: str, age: int) -> User:
    try:
        edit_user = users[user_id - 1]
        edit_user.username = username
        edit_user.age = age
        return edit_user
    except IndexError:
        raise HTTPException(status_code=404, detail='User was not found')


@app.delete('/user/{user_id}')
async def delete_user(user_id: int) -> User:
    try:
        temp_user = users[user_id - 1]
        users.pop(user_id - 1)
        return temp_user
    except IndexError:
        raise HTTPException(status_code=404, detail='User was not found')
    