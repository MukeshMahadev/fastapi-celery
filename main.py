from fastapi import FastAPI, WebSocket
import uvicorn
from routers.tasks import tasks_router


app = FastAPI()

app.include_router(tasks_router, prefix="/tasks", tags=["tasks"])


@app.get("/healthcheck")
async def healthcheck():
    # Enqueue the task
    return {"message": "Server is up and running"}

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=7777)
