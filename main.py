from fastapi import FastAPI
from routes import comercios

app = FastAPI()
comercios.init_app(app)