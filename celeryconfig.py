from celery import Celery
from celery.schedules import crontab


# Initialize Celery app
celery_app = Celery(
    "news_fetcher",
    broker="redis://localhost:6379/0",  # Use Redis as a broker
    backend="redis://localhost:6379/0"  # Use Redis as a result backend
)

# Celery configurations
celery_app.conf.update(
    task_serializer="json",
    accept_content=["json"],
    result_serializer="json",
    timezone="UTC",
    enable_utc=True,
)

celery_app = Celery(
    "fastapi-celery-news_fetcher", 
    broker="redis://localhost:6379/0", 
    backend="redis://localhost:6379/0"
)

# Import tasks to register them
import app.tasks

celery_app.conf.beat_schedule = {
    "fetch-news-every-minute": {
        "task": "app.tasks.fetch_and_store_news",
        "schedule": crontab(minute="*"),
    },
}
