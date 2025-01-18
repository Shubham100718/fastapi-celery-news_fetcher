import requests
from app.database import get_connection
from celeryconfig import celery_app


NEWS_API_KEY = "85b3dc6080d843d9965af392b108fd39"
NEWS_API_URL = "https://newsapi.org/v2/top-headlines"

@celery_app.task(name="app.tasks.fetch_and_store_news")
def fetch_and_store_news():
    try:
        # Fetch news data
        params = {"apiKey": NEWS_API_KEY, "country": "us", "category": "business"}
        response = requests.get(NEWS_API_URL, params=params)
        response.raise_for_status()
        articles = response.json().get("articles", [])
        # print(articles)

        # Store news in the database
        connection = get_connection()
        with connection.cursor() as cursor:
            for article in articles:
                cursor.execute("""
                INSERT INTO news (source_id, source_name, author, title, description, url, urlToImage, published_at, content)
                VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
                """, (
                    article.get('source').get('id'),
                    article.get('source').get('name'),
                    article.get("author"),
                    article.get("title"),
                    article.get("description"),
                    article.get("url"),
                    article.get("urlToImage"),
                    article.get("publishedAt"),
                    article.get("content"),
                ))
            connection.commit()
        connection.close()

        return f"Fetched and stored {len(articles)} articles."
    except Exception as err:
        return f"Error in fetch_and_store_news: {str(err)}"

