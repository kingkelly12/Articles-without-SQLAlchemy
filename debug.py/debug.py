from models.author import Author
from models.magazine import Magazine
from models.article import Article
from db.connection import get_connection

def debug():
    print("Debug console for Articles-Authors-Magazines system")
    print("Available classes: Author, Magazine, Article")
    print("Example usage:")
    print("  author = Author(name='John Doe')")
    print("  author.save()")
    print("  magazine = Magazine(name='Tech Today', category='Technology')")
    print("  magazine.save()")
    print("  article = Article(title='Python Programming', author_id=author.id, magazine_id=magazine.id)")
    print("  article.save()")

if __name__ == "__main__":
    debug()