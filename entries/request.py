from models.entries import Entry
import sqlite3
import json

def get_all_entries():
	
	with sqlite3.connect("./dailyjournal.db") as conn:

		conn.row_factory = sqlite3.Row
		db_cursor = conn.cursor()

		db_cursor.execute("""
		SELECT 
			* 
		FROM Entries
		""")

		entries = []

		dataset = db_cursor.fetchall()

		for row in dataset:
			entry = Entry(row['id'], row['date'], row['concept'], row['entry'], row['mood_id'])
			entries.append(entry.__dict__)
	
	return json.dumps(entries)
