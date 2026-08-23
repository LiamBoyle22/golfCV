from fastapi import FastAPI
from workers.celery_app import run_pose_inference, ping_metrics_task

app = FastAPI()

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.get("/test-real-inference/{clip_id}")
def test_inference_worker(clip_id: str):
    result = run_pose_inference.delay(clip_id)
    return {"task_id": result.id}

@app.get("/test-metrics")
def test_metrics_worker():
    result = ping_metrics_task.delay()
    return {"message": "Metrics worker pinged", "result": result.get()}