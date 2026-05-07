"""
Database migration script to add timestamp columns to existing tables
"""
from sqlalchemy import text
from database import engine

def add_timestamp_columns():
    """Add create_ts, update_ts, delete_ts columns to existing tables"""
    
    with engine.connect() as connection:
        # Add columns to users table
        try:
            connection.execute(text("""
                ALTER TABLE users 
                ADD COLUMN IF NOT EXISTS create_ts TIMESTAMP,
                ADD COLUMN IF NOT EXISTS update_ts TIMESTAMP,
                ADD COLUMN IF NOT EXISTS delete_ts TIMESTAMP
            """))
            print("Added timestamp columns to users table")
        except Exception as e:
            print(f"Error adding columns to users: {e}")
        
        # Add columns to tasks table
        try:
            connection.execute(text("""
                ALTER TABLE tasks 
                ADD COLUMN IF NOT EXISTS create_ts TIMESTAMP,
                ADD COLUMN IF NOT EXISTS update_ts TIMESTAMP,
                ADD COLUMN IF NOT EXISTS delete_ts TIMESTAMP
            """))
            print("Added timestamp columns to tasks table")
        except Exception as e:
            print(f"Error adding columns to tasks: {e}")
        
        # Add columns to comments table
        try:
            connection.execute(text("""
                ALTER TABLE comments 
                ADD COLUMN IF NOT EXISTS create_ts TIMESTAMP,
                ADD COLUMN IF NOT EXISTS update_ts TIMESTAMP,
                ADD COLUMN IF NOT EXISTS delete_ts TIMESTAMP
            """))
            print("Added timestamp columns to comments table")
        except Exception as e:
            print(f"Error adding columns to comments: {e}")
        
        connection.commit()
        print("Migration completed successfully!")

if __name__ == "__main__":
    add_timestamp_columns()
