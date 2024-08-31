from fastapi import FastAPI

app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}

@app.get('/users')
async def get_all_users() -> dict:
    return users


@app.post('/user/{username}/{age}')
async def create_user(username: str, age: int) -> str:
    current_index = str(int(max(users, key=int))+1)
    current_user = f'Имя: {username}, возраст {age}'
    users[current_index] = current_user
    return f'User {current_index} is registered'


@app.put('/user/{user_id}/{username}/{age}')
async def update_user(user_id: int, username: str, age: int) -> str:
    users[user_id] = f'Имя: {username}, возраст {age}'
    return f'The user {user_id} is updated'


@app.delete('/user/{user_id}')
async def delete_user(user_id: str):
    users.pop(user_id)
