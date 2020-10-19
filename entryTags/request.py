from models import EntryTag
import sqlite3
import json

def get_all_entry_tags():
  with sqlite3.connect("./dailyjournal.db") as conn:
    conn.row_factory = sqlite3.Row
    db_cursor = conn.cursor()

    db_cursor.execute("""
    SELECT 
      et.id,
      et.entry_id,
      et.tag_id
    FROM EntryTags et
    """)

    entryTags = []
    dataset = db_cursor.fetchall()

    for row in dataset:
      entryTag = EntryTag(row['id'], row['entry_id'], row['tag_id'])
      entryTags.append(entryTag.__dict__)
  
  return json.dumps(entryTags)