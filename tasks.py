from celery import Celery
import time
import os

celery_app = Celery(
    "tasks",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/0"
)
# celery_app.conf.update(task_always_eager=True)

@celery_app.task
def task(type: int):
    path = "common"
    file = f"{path}/data.txt"

    with open(file, "r", encoding="utf-8") as f:
        data = f.read()
    time.sleep(type)
    return {"type": type, "data": data}
