



from app.database import get_connection

conn = get_connection()

cursor = conn.cursor()

cursor.execute("""

CREATE TABLE IF NOT EXISTS analysis_history(

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    filename TEXT,

    prediction TEXT,

    confidence REAL,

    risk TEXT,

    duration REAL,

    sample_rate INTEGER,

    analysis_time REAL,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

)

""")

conn.commit()

conn.close()

print("Database Created Successfully!")