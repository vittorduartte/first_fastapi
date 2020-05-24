from typing import List
from pydantic import BaseModel

class ComercioBase(BaseModel):
    nome: str
    local: str

class ComercioCreate(ComercioBase):
    pass

class Comercio(ComercioBase):
    id: int

    class Config:
        orm_mode=True

