from uuid import UUID

from pydantic import BaseModel

from iad_sistem_liza.db.db import TourSample, Session_maker, Client, Tour
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from typing import List


app = FastAPI()

def get_db():
    db = Session_maker()
    try:
        yield db
    finally:
        db.close()


# Маршрут для получения всех записей TourSample
@app.get("/toursample/", response_model=List)
def get_all_tour_samples(db: Session = Depends(get_db)):
    tour_samples = db.query(TourSample).all()
    if not tour_samples:
        raise HTTPException(status_code=404, detail="Not found")
    return tour_samples


@app.get("/client/", response_model=List)
def get_all_clients(db: Session = Depends(get_db)):
    client_samples = db.query(Client).all()
    if not client_samples:
        raise HTTPException(status_code=404, detail="Not found")
    return client_samples

@app.get("/tour/", response_model=List)
def get_all_tours(db: Session = Depends(get_db)):
    tours = db.query(Tour).all()
    if not tours:
        raise HTTPException(status_code=404, detail="Not found")
    return tours