from sqlalchemy.orm import Session
from models.comercios import Comercio as Comercio_Model
from schemas.comercios import ComercioCreate as Comercio_Schema

def get_comercio(db: Session, comercio_id: int):
    return db.query(Comercio_Model).filter(Comercio_Model.id == comercio_id).first()

def get_comercios(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Comercio_Model).offset(skip).limit(limit).all()

def create_comercio(db: Session, comercio: Comercio_Schema):
    db_comercio = Comercio_Model(nome=comercio.nome, local=comercio.local)
    db.add(db_comercio)
    db.commit()
    db.refresh(db_comercio)
    return db_comercio 
