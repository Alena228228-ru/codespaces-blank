from fastapi import FastAPI

from service.any_of_service import clients

app = FastAPI()

@app.get("/say")
async def say_hello():
    return 'Hello world!'

@app.get("/get_client")
async def get_clients():
    return clients.get_client()