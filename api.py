from fastapi import FastAPI
from celery import group
from tasks import task_a, task_b, task_c, task_d, task_e

app = FastAPI()

@app.get("/run-tasks")
async def run_tasks():
    """ 느린 기능과 빠른 기능을 분리하여 실행 """
    fast_tasks = group(task_a.s(), task_b.s()).apply_async(queue="fast_tasks")
    slow_tasks = group(task_c.s(), task_d.s(), task_e.s()).apply_async(queue="slow_tasks")

    return {"fast_task_id": fast_tasks.id, "slow_task_id": slow_tasks.id}
