from fastapi import APIRouter, WebSocket
from celery_q.celery_worker import background_task, celery_app
from celery.result import AsyncResult
import asyncio

tasks_router = APIRouter()


@tasks_router.post("")
async def add_task(arg1: str, arg2: int):
    # Enqueue the task
    task = background_task.delay(int(arg1), int(arg2))
    return {"task_id": task.id, "message": "Task added to Celery"}


@tasks_router.get("/{task_id}/status")
async def get_task_status(task_id: str):
    # Get the status of the Celery task
    result = AsyncResult(task_id, app=celery_app)
    return {"status": result.state}


@tasks_router.websocket("/ws/{task_id}")
async def websocket_endpoint(websocket: WebSocket, task_id: str):
    await websocket.accept()

    # Get the task result asynchronously
    result = AsyncResult(task_id, app=celery_app)

    while True:
        if result.ready():
            break
        await websocket.send_text(result.state)
        await asyncio.sleep(2)

    # Task is ready, send the final result
    if result.successful():
        await websocket.send_text(str(result.state))
        await websocket.send_text(str(result.result))
        await websocket.close()
    else:
        await websocket.send_text(result.state)