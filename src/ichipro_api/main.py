from fastapi import FastAPI
import uvicorn

from router.user import user  # type: ignore

print("> main.py")

app = FastAPI()


@app.get("/")
async def get_data():
    response = {"message": "Web API is running."}
    return response


@app.get("/api/v1/")
async def get_data():
    response = {"message": "Web API is running."}
    return response


app.include_router(user.router, prefix="/api/v1/auth")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=80, log_level="debug")
