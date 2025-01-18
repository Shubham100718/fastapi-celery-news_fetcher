import pymysql
import pymysql.cursors


# Database connection details
DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "",
    "database": "mydb",
}

def get_connection():
    return pymysql.connect(
        host=DB_CONFIG["host"],
        user=DB_CONFIG["user"],
        password=DB_CONFIG["password"],
        database=DB_CONFIG["database"],
        cursorclass=pymysql.cursors.DictCursor,
    )

def create_news_table():
    connection = get_connection()
    with connection.cursor() as cursor:
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS news (
            id INT AUTO_INCREMENT PRIMARY KEY,
            source_id VARCHAR(255),
            source_name VARCHAR(255),
            author VARCHAR(255),
            title VARCHAR(255),
            description TEXT,
            url VARCHAR(255),
            urlToImage VARCHAR(255),
            published_at DATETIME,
            content TEXT
        )
        """)
        connection.commit()
    connection.close()

# Ensure table exists
create_news_table()

