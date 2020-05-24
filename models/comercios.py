from sqlalchemy import Column, Integer, String
from ext.database import Base

class Comercio(Base):
    __tablename__="comercios"

    id = Column(Integer, primary_key=True)
    nome = Column(String(120), nullable=False)
    local = Column(String(120), nullable=False)



