from .connection import get_connection

def create_tables():
    """Create database tables from schema.sql"""
    conn = get_connection()
    cursor = conn.cursor()
    
    with open('db/schema.sql', 'r') as f:
        schema = f.read()
    
    cursor.executescript(schema)
    conn.commit()
    conn.close()