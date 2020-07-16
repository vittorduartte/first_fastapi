from sqlalchemy import Column, Integer, String
from ext.database import Base

class Cliente(Base):
    __tablename__="clientes"

    id = Column(Integer, primary_key=True)
    nome = Column(String(120), nullable=False)
    contato = Column(String(11), nullable=False)



