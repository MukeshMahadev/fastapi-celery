from fastapi import FastAPI
from celery import Celery
import uvicorn
app = FastAPI()

# Configure Celery
celery = Celery(
    'tasks',
    broker='redis://localhost:6379/0'
)


# Define a Celery task
@celery.task
def background_task(arg1, arg2):
    # Task logic goes here
    print(f"Background task executed with args: {arg1}, {arg2}")


# FastAPI endpoint to add tasks to Celery
@app.post("/task")
async def add_task(arg1: str, arg2: int):
    # Enqueue the task
    background_task.delay(arg1, arg2)
    return {"message": "Task added to Celery"}


# FastAPI endpoint to add tasks to Celery
@app.get("/healthcheck")
async def add_task():
    # Enqueue the task
    return {"message": "Server is up and running"}

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=7777)
