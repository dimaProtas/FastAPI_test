from fastapi import FastAPI, HTTPException, Query, Body
import redis

app = FastAPI()

# Подключение к Redis
redis_client = redis.StrictRedis(host='fastapi_proj_redis_1', port=6379, db=0)


@app.post("/write_data")
def write_data(phone: str = Body(...), address: str = Body(...)):
    redis_client.set(phone, address)
    return {"message": "Данные успешно записаны!"}


@app.put("/write_data")
def update_data(phone: str = Body(...), address: str = Body(...)):
    if not redis_client.exists(phone):
        raise HTTPException(status_code=404, detail="Нет такого номера!")
    redis_client.set(phone, address)
    return {"message": "Данные успешно обновлены!"}


@app.get("/check_data")
def check_data(phone: str = Query(...)):
    address = redis_client.get(phone)
    if address is None:
        raise HTTPException(status_code=404, detail="Нет такого номера!")
    return {"phone": phone, "address": address.decode('utf-8')}
