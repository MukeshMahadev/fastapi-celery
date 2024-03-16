import time

from celery import Celery

celery_app = Celery('tasks', broker='redis://localhost:6379/0', backend='redis://localhost:6379/0')


@celery_app.task()
def background_task(a, b):
    time.sleep(30)
    a = int(a)
    b = int(b)
    for i in range(a, b):
        print(i)
    return {"number": a+b}