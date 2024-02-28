from datetime import datetime
from typing import Union
from fastapi import Depends, FastAPI, Body, HTTPException, Request
from models import Base,  SessionLocal
from services import engine
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse, FileResponse
from fastapi.middleware.cors import CORSMiddleware
import crud
import models
from schemas import Info
from statistics import median

# creating table
Base.metadata.create_all(bind=engine)

app = FastAPI()
origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


#adding record to database
@app.post("/", status_code=201)
async def create_item(request: Request, item: Info, db: Session = Depends(get_db)):

    # saving data to database
    item_id = crud.save_item_to_db(db, item)

    return 'ok'

# function to make analitics of x,y,x for each device
def analitics(x):
    x_min = min(x)
    x_max = max(x)
    x_len = len(x)
    x_sum = sum(x)
    x_med = median(x)
    return {
        'Минимальное значение': x_min,
        'Максимальное значение': x_max,
        'Количество': x_len,
        'Сумма': x_sum,
        'Медиана': x_med
    }

# get statistics from device for all time
@app.get("/device/{device_id}", response_model=None)
def read_user(device_id: str, db: Session = Depends(get_db)):
    db_user = crud.get_device(db, device_id=device_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    
    y_ = []
    x_ = []
    z_ = []
    for i in db_user:
        y_.append(i.y)
        x_.append(i.x)
        z_.append(i.z)
    
    ans = {}
    ans['x'] = analitics(x_)
    ans['y'] = analitics(y_)
    ans['z'] = analitics(z_)

    return ans

# get statistics from device in certain time
@app.get("/device/{device_id}/{start_datetime}/{end_datetime}", response_model=None)
def read_device_time(device_id: str, start_datetime: datetime, end_datetime: datetime, db: Session = Depends(get_db)):
    db_user = crud.get_device_time(db, device_id=device_id, start_datetime=start_datetime, end_datetime=end_datetime)
    if not db_user:
        raise HTTPException(status_code=404, detail="There is no recordings in this time")

    y_ = []
    x_ = []
    z_ = []
    for i in db_user:
        y_.append(i.y)
        x_.append(i.x)
        z_.append(i.z)
    
    ans = {}
    ans['x'] = analitics(x_)
    ans['y'] = analitics(y_)
    ans['z'] = analitics(z_)

    return ans
    
    





