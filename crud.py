from datetime import datetime
from sqlalchemy import and_
from sqlalchemy.orm import Session
import models
import schemas
import json
from bson import json_util
import pandas as pd
from services import engine


# adding a record to database
def save_item_to_db(db: Session, item: schemas.Info):
    # creating new element
    new_item = models.Info(device=item.device, date=item.date, x=item.x, y=item.y, z=item.z)

    # adding element to session
    db.add(new_item)

    # saving changes to database
    db.commit()

    db.refresh(new_item)

    return new_item.id



def get_device(db: Session, device_id: str):
    res =  db.query(models.Info).filter(models.Info.device == device_id).all()
    return res

def get_device_time(db: Session, device_id: str, start_datetime: datetime, end_datetime: datetime):
    res = db.query(models.Info).filter(and_(models.Info.device == device_id, models.Info.date >= start_datetime, models.Info.date <= end_datetime)).all()
    return res