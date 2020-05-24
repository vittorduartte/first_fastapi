# Primeira API com FastAPI
#### Uma aplicação escrita em Python utilizando a tecnologia FastAPI para desenvolvimento de uma API, incluindo conexão ao banco de dados SQLite.

## Instalação
>**Requirements:** Python 3.7.x, Pipenv;

```shell 
git clone https://github.com/vittorduartte/first_fastapi

cd first_fastapi

pipenv shell
```

## Executando a aplicação

```shell
uvicorn main:app --reload
```

## Arquitetura V0

```shell
.
├── database
│   └── banco.db
├── ext
│   ├── database.py
│   └── __init__.py
├── main.py
├── models
│   ├── comercios.py
│   └── __init__.py
├── Pipfile
├── Pipfile.lock
├── README.md
├── routes
│   ├── comercios.py
│   └── __init__.py
├── rules
│   ├── crud.py
│   └── __init__.py
└── schemas
    ├── comercios.py
    └── __init__.py

```

## Ferramentas

* **FastAPI by Tiangolo** - https://fastapi.tiangolo.com/pt/

* **SQLAlchemy** - https://www.sqlalchemy.org/

