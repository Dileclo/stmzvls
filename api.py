from pymongo import MongoClient
from pydantic import BaseModel
from fastapi import FastAPI,HTTPException,APIRouter
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from typing import List
import random


client = MongoClient("localhost", 27017)
db = client["test-database"]

router = APIRouter()

users = db["users"]
attendance_collection = db['attendance']
class User(BaseModel):
    name: str
    family_name: str
    email: str
    phone: str 
    position:str
    second_name:str
    id:str

class UserID(BaseModel):
    id:str

class Attendance(BaseModel):
    user_id:str
    date:str
    is_present:bool

@router.get("/")
def read_root():
    return {"Hello": "World"}


@router.get("/get_users")
def get_users():
    r = list(users.find({}, {"_id": 0}))

    return JSONResponse(content={"data":jsonable_encoder(r)})

@router.get("/get_users_by_date")
def get_users_by_date(date:str):
    r = list(users.find({}, {"_id": 0}))
    a = list(attendance_collection.find({'date':date}))
    attendance_dict = {record['user_id']: record['is_present'] for record in a}
    print(attendance_dict)
    for i in r:
        i['is_present'] = attendance_dict.get(i['id'],False)
    print(r)
    return JSONResponse(content={"data":jsonable_encoder(r)})

@router.post("/update_attendance")
def update_attendance(attendance: Attendance):
    attendance_record = attendance_collection.find_one({
        "user_id": attendance.user_id,
        "date": attendance.date
    })
    
    if attendance_record:
         attendance_collection.update_one(
            {"_id": attendance_record["_id"]},
            {"$set": {"is_present": attendance.is_present}}
        )
    else:
         attendance_collection.insert_one(attendance.dict())
    return "Hello world"


@router.get('/get_user/{id}')
def get_user_by_id(id:str):
    r = users.find_one({"id":id},{"_id": 0})
    print(r)
    return JSONResponse(content=jsonable_encoder(r))

@router.post("/add_user")
async def add_user(user: User):
    r = users.find_one({'phone':user.phone})
    if r: raise HTTPException(status_code=404, detail="Такой пользователь уже существует")
    p = users.insert_one({'name':user.name,'family_name':user.family_name,'email':user.email,'phone':user.phone,'position':user.position,'second_name':user.second_name,'id':str(random.randint(1,100000000000))})
    return ""

@router.post("/delete_user")
async def delete_user(user_id: UserID):
    r = users.find_one({'id': user_id.id})
    if r:
        users.delete_one({'id': user_id.id})
        return {"message": "Успешно удалено"}
    else:
        raise HTTPException(status_code=404, detail="Пользователь не найден")
    