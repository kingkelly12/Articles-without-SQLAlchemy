from models.author import Author
from models.magazine import Magazine
from models.article import Article
from db.connection import get_connection

def setup_sample_data():
    """Create sample data for demonstration purposes"""
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("DELETE FROM articles")
    cursor.execute("DELETE FROM authors")
    cursor.execute("DELETE FROM magazines")
    conn.commit()
    
    authors = [
        Author(name="J.K. Rowling"),
        Author(name="Stephen King"),
        Author(name="George R.R. Martin"),
        Author(name="Agatha Christie")
    ]
    for author in authors:
        author.save()
    
    magazines = [
        Magazine(name="Fantasy Today", category="Fantasy"),
        Magazine(name="Mystery Monthly", category="Mystery"),
        Magazine(name="Horror Digest", category="Horror"),
        Magazine(name="Best Sellers", category="General")
    ]
    for magazine in magazines:
        magazine.save()
        
    articles = [
        {"title": "Harry Potter and the Philosopher's Stone", "author": "J.K. Rowling", "magazine": "Fantasy Today"},
        {"title": "The Shining", "author": "Stephen King", "magazine": "Horror Digest"},
        {"title": "A Game of Thrones", "author": "George R.R. Martin", "magazine": "Fantasy Today"},
        {"title": "Murder on the Orient Express", "author": "Agatha Christie", "magazine": "Mystery Monthly"},
        {"title": "The Casual Vacancy", "author": "J.K. Rowling", "magazine": "Best Sellers"},
        {"title": "It", "author": "Stephen King", "magazine": "Horror Digest"},
        {"title": "And Then There Were None", "author": "Agatha Christie", "magazine": "Mystery Monthly"},
        {"title": "The Cuckoo's Calling", "author": "J.K. Rowling", "magazine": "Best Sellers"}
    ]
    
    for article_data in articles:
        author = Author.find_by_name(article_data["author"])
        magazine = Magazine.find_by_name(article_data["magazine"])
        article = Article(
            title=article_data["title"],
            author_id=author.id,
            magazine_id=magazine.id
        )
        article.save()
    
    conn.close()

def run_demo_queries():
    """Run and print results of example queries"""
    print("\n=== DEMONSTRATION QUERIES ===\n")
    
    # 1. Get all articles by J.K. Rowling
    print("1. All articles by J.K. Rowling:")
    jk_rowling = Author.find_by_name("J.K. Rowling")
    for article in jk_rowling.articles():
        print(f"- {article.title}")
    print()
    
    # 2. Find all magazines J.K. Rowling has contributed to
    print("2. Magazines J.K. Rowling has contributed to:")
    for magazine in jk_rowling.magazines():
        print(f"- {magazine.name} ({magazine.category})")
    print()
    
    # 3. Get all authors who have written for Fantasy Today
    print("3. Authors who have written for Fantasy Today:")
    fantasy_today = Magazine.find_by_name("Fantasy Today")
    for author in fantasy_today.contributors():
        print(f"- {author.name}")
    print()
    
    # 4. Find magazines with articles by at least 2 different authors
    print("4. Magazines with articles by at least 2 authors:")
    for magazine in Magazine.magazines_with_multiple_authors():
        print(f"- {magazine.name} ({magazine.category})")
        print("  Contributors:")
        for author in magazine.contributors():
            print(f"  - {author.name}")
    print()
    
    # 5. Count the number of articles in each magazine
    print("5. Article count per magazine:")
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT m.name, COUNT(a.id) as article_count
        FROM magazines m
        LEFT JOIN articles a ON m.id = a.magazine_id
        GROUP BY m.id
        ORDER BY article_count DESC
    """)
    for row in cursor.fetchall():
        print(f"- {row['name']}: {row['article_count']} articles")
    conn.close()
    print()
    
    # 6. Find the author who has written the most articles
    print("6. Author with most articles:")
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT a.name, COUNT(ar.id) as article_count
        FROM authors a
        JOIN articles ar ON a.id = ar.author_id
        GROUP BY a.id
        ORDER BY article_count DESC
        LIMIT 1
    """)
    row = cursor.fetchone()
    print(f"- {row['name']} with {row['article_count']} articles")
    conn.close()
    print()
    
    # 7. Show contributing authors (with >2 articles) for each magazine
    print("7. Contributing authors (with >2 articles) per magazine:")
    for magazine in Magazine.all():
        contributing_authors = magazine.contributing_authors()
        if contributing_authors:
            print(f"- {magazine.name}:")
            for author in contributing_authors:
                print(f"  - {author.name}")
    print()

def main():
    print("Setting up sample data...")
    setup_sample_data()
    
    run_demo_queries()
    
    print("=== DEMONSTRATION COMPLETE ===")

if __name__ == "__main__":
    main()