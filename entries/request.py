from models.moods import Mood
from models.entries import Entry
import sqlite3
import json

def get_all_entries():
	
	with sqlite3.connect("./dailyjournal.db") as conn:

		conn.row_factory = sqlite3.Row
		db_cursor = conn.cursor()

		db_cursor.execute("""
		SELECT 
			e.id,
			e.date,
			e.concept,
			e.entry,
			e.mood_id,
			m.name AS mood_name
		FROM Entries e
		JOIN Moods m
			ON e.mood_id = m.id
		""")

		entries = []

		dataset = db_cursor.fetchall()

		for row in dataset:
			entry = Entry(row['id'], row['date'], row['concept'], row['entry'], row['mood_id'])
			mood = Mood(row['mood_id'], row['mood_name'])
			entry.mood = mood.__dict__
			entries.append(entry.__dict__)
	
	return json.dumps(entries)

def get_single_entry(entryId):
	with sqlite3.connect("./dailyjournal.db") as conn:
		conn.row_factory = sqlite3.Row
		db_cursor = conn.cursor()

		db_cursor.execute("""
		SELECT 
			e.id,
			e.date,
			e.concept,
			e.entry,
			e.mood_id,
			m.name AS mood_name
		FROM Entries e
		JOIN Moods m
			ON e.mood_id = m.id
		WHERE e.id = ?
		""", ( entryId, ))

		data = db_cursor.fetchone()
		entry = Entry(data['id'], data['date'], data['concept'], data['entry'], data['mood_id'])
		mood = Mood(data['mood_id'], data['mood_name'])
		entry.mood = mood.__dict__

	return json.dumps(entry.__dict__)

def create_entry(newEntry):
	with sqlite3.connect("./dailyjournal.db") as conn:
		db_cursor = conn.cursor()
		db_cursor.execute("""
		INSERT INTO Entries
			( date, concept, entry, mood_id )
		VALUES
			( ?, ?, ?, ? );
		""" , (newEntry['date'], newEntry['concept'], newEntry['entry'], newEntry['moodId']) )

		id = db_cursor.lastrowid
		newEntry['id'] = id

	return json.dumps(newEntry)

def delete_entry(entryId):
	with sqlite3.connect("./dailyjournal.db") as conn:
		db_cursor = conn.cursor()
		
		db_cursor.execute("""
		DELETE 
		FROM Entries AS e
		WHERE e.id = ?
		""", ( entryId, ))

		db_cursor.execute("""
		DELETE 
		FROM EntryTags AS et
		WHERE et.entry_id = ?
		""", ( entryId, ))


def update_journal_entry(id, updatedEntry):
	with sqlite3.connect("./dailyjournal.db") as conn:
		db_cursor = conn.cursor()
		
		db_cursor.execute("""
		UPDATE Entries
			SET 
				date = ?,
				concept = ?,
				entry = ?,
				mood_id = ?
			WHERE id = ?
		""", (updatedEntry['date'], updatedEntry['concept'], 
		updatedEntry['entry'], updatedEntry['moodId'], id ) )	

		rows_affected = db_cursor.rowcount

		if rows_affected == 0:
			return False 
		else: 
			return True
