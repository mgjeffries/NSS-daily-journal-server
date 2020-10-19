from models import Tag
import sqlite3
import json

def get_all_tags():
  with sqlite3.connect("./dailyjournal.db") as conn:
    conn.row_factory = sqlite3.Row
    db_cursor = conn.cursor()

    db_cursor.execute("""
    SELECT 
      t.id,
      t.subject
    FROM Tags t
    """)

    tags = []
    dataset = db_cursor.fetchall()

    for row in dataset:
      tag = Tag( row['id'], row['subject'])
      tags.append(tag.__dict__)
    
    return json.dumps(tags)


def create_tag(newTag):
  with sqlite3.connect("./dailyjournal.db") as conn:
    db_cursor = conn.cursor()
    db_cursor.execute("""
    INSERT INTO Tags
      ( subject )
    VALUES
      ( ? );
    """ , (newTag['subject'], ) )

    id = db_cursor.lastrowid
    newTag['id'] = id
  return json.dumps(newTag)