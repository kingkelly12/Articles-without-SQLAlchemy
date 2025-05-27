from .connection import get_connection
from ..models import Author, Magazine, Article

def seed_database():
    """Populate database with sample data"""
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("DELETE FROM articles")
    cursor.execute("DELETE FROM authors")
    cursor.execute("DELETE FROM magazines")
    conn.commit()
    
    # Sample authors
    authors = [
        Author(name="J.K. Rowling"),
        Author(name="Stephen King"),
        Author(name="George R.R. Martin")
    ]
    for author in authors:
        author.save()
    # Sample magazines
    magazines = [
        Magazine(name="Fantasy Today", category="Fantasy"),
        Magazine(name="Horror Digest", category="Horror"),
        Magazine(name="Best Sellers", category="General")
    ]
    for magazine in magazines:
        magazine.save()
    # Sample articles
    articles = [
        {"title": "Harry Potter", "author": "J.K. Rowling", "magazine": "Fantasy Today"},
        {"title": "The Shining", "author": "Stephen King", "magazine": "Horror Digest"},
        {"title": "A Game of Thrones", "author": "George R.R. Martin", "magazine": "Fantasy Today"}
    ]
    
    for article in articles:
        author = Author.find_by_name(article["author"])
        magazine = Magazine.find_by_name(article["magazine"])
        Article(
            title=article["title"],
            author_id=author.id,
            magazine_id=magazine.id
        ).save()
    
    conn.close()