from fastapi import FastAPI
from celery import group
from tasks import task
import uvicorn

app = FastAPI()

@app.get("/")
async def run_tasks():
    """ 느린 기능과 빠른 기능을 분리하여 실행 """
    tasks = group(task.si(i) for i in range(8)).apply_async()
    
    results = tasks.get()  # Wait for all tasks to complete and get results
    
    for result in results:
        print(result)
    
    return {"tasks": results}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
