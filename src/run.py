from fastapi import FastAPI
from src.app.main.app_factory import create_app

app = create_app()
