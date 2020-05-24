from fastapi import APIRouter, Depends
from typing import List
from sqlalchemy.orm import Session
from ext.database import SessionLocal, engine, get_db, engine
from models.comercios import Comercio as Comercio_Model
from schemas.comercios import Comercio, ComercioCreate
from rules import crud
from models.comercios import Base

Base.metadata.create_all(bind=engine)
router = APIRouter()

def init_app(app):

    @router.get('/comercios/', response_model=List[Comercio])
    def read_comercios(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
        comercios = crud.get_comercios(db, skip=skip, limit=limit)
        return comercios
    
    @router.post('/comercios/', response_model=Comercio)
    def create_comercio(comercio: ComercioCreate, db: Session = Depends(get_db)):
        return crud.create_comercio(db=db, comercio=comercio)

    app.include_router(router)