from celery import Celery

celery_app = Celery(
    "yolfcv",
    broker = "redis://redis:6379/0",
    backend = "redis://redis:6379/0",
)

@celery_app.task(queue = "inference")
################
def ping_inference_task():
    return "pong from inference worker"

@celery_app.task(queue = "metrics")
################
def ping_metrics_task():
    return "pong from metrics worker"