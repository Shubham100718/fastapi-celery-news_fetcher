# FASTAPI CELERY NEWS FETCHER

What does this project do?
 * Use the News API (https://newsapi.org/) to fetch news data.
 * Then a periodic task that automatically runs every minute using Celery and Celery Beat.
 * Then this task stores the results in the MySQL database.


## How to start the application?

### Run the FastAPI App (Optional)
```
uvicorn main:app --reload
```

### Start the Celery worker
```
celery -A celeryconfig.celery_app worker --loglevel=info
```

### Start the Celery beat
```
celery -A celeryconfig.celery_app beat --loglevel=info
```
