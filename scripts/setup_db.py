from db.connection import get_connection

def setup_database():
    conn = get_connection()
    cursor = conn.cursor()
    
   
    with open('db/schema.sql', 'r') as f:
        schema = f.read()
    cursor.executescript(schema)
    
    conn.commit()
    conn.close()
    print("Database setup complete!")

if __name__ == "__main__":
    setup_database()