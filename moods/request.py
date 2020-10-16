from models import Mood
import sqlite3
import json

def get_all_moods():
  with sqlite3.connect("./dailyjournal.db") as conn:
    conn.row_factory = sqlite3.Row
    db_cursor = conn.cursor()

    db_cursor.execute("""
    SELECT 
      m.id,
      m.name
    FROM Moods m
    """)

    moods = []
    dataset = db_cursor.fetchall()

    for row in dataset:
      mood = Mood(row['id'], row['name'])
      moods.append(mood)
  
  return json.dumps(moods.__dict__)