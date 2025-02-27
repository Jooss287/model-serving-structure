from celery import Celery
import time

celery_app = Celery(
    "tasks",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/0"
)

@celery_app.task(queue="fast_tasks")  # 빠른 작업을 위한 큐
def task_a():
    time.sleep(1)
    return "A 완료"

@celery_app.task(queue="fast_tasks")
def task_b():
    time.sleep(2)
    return "B 완료"

@celery_app.task(queue="slow_tasks")  # 느린 작업을 위한 큐
def task_c():
    time.sleep(3)
    return "C 완료"

@celery_app.task(queue="slow_tasks")
def task_d():
    time.sleep(4)
    return "D 완료"

@celery_app.task(queue="slow_tasks")
def task_e():
    time.sleep(5)
    return "E 완료"
