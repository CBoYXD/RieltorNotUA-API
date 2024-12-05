from fastapi import FastAPI

# Some logic here

def create_app() -> FastAPI:
    app = FastAPI()

    @app.get("/ping")
    async def ping_pong() -> str:
        return "pong"

    return app
