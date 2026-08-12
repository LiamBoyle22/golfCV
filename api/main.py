from fastapi import FastAPI
from workers.celery_app import ping_metrics_task, ping_inference_task

app = FastAPI()

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.get("/test-inference")
def test_inference_worker():
    result = ping_inference_task.delay()
    return {"message": "Inference worker pinged", "result": result.get()}

@app.get("/test-metrics")
def test_metrics_worker():
    result = ping_metrics_task.delay()
    return {"message": "Metrics worker pinged", "result": result.get()}