CREATE TABLE 'Moods' (
  'id' INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  'name' TEXT NOT NULL
)


CREATE TABLE 'Entries' (
  'id' INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  'date' TEXT NOT NULL,
  'concept' TEXT NOT NULL,
  'entry' TEXT NOT NULL,
  'mood_id' INTEGER NOT NULL,
  FOREIGN KEY('mood_id') REFERENCES 'Moods'('id')
)

CREATE TABLE 'Tags' (
  'id' INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  'name' TEXT NOT NULL
)

CREATE TABLE 'EntryTags' (
  'id' INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  'entry_id' INTEGER NOT NULL,
  'tag_id' INTEGER NOT NULL,
  FOREIGN KEY('entry_id') REFERENCES 'Entries'('id'),
  FOREIGN KEY('tag_id') REFERENCES 'Tags'('id')
)

INSERT INTO 'Moods' VALUES (null, 'happy');
INSERT INTO 'Moods' VALUES (null, 'meh');
INSERT INTO 'Moods' VALUES (null, 'sad');
INSERT INTO 'Moods' VALUES (null, 'ominous');
INSERT INTO 'Moods' VALUES (null, 'optimistic');
INSERT INTO 'Moods' VALUES (null, 'adventurous');

INSERT INTO 'Entries' VALUES (null, '07/06/2020', 'Start Day', 'John Talked to the class most of the day', 1);
INSERT INTO 'Entries' VALUES (null, '07/08/2020', 'HTML & CSS', 'Jumped in to creating pages with css and flexbox. Feeling overwhelmed', 1);

INSERT INTO 'Tags' VALUES (null, 'API');
INSERT INTO 'Tags' VALUES (null, 'components');
INSERT INTO 'Tags' VALUES (null, 'fetch');
INSERT INTO 'Tags' VALUES (null, 'tagging');
INSERT INTO 'Tags' VALUES (null, 'componenet state');
INSERT INTO 'Tags' VALUES (null, 'character counter');
INSERT INTO 'Tags' VALUES (null, 'decoupling');
INSERT INTO 'Tags' VALUES (null, 'CRUD');

INSERT INTO 'EntryTags' VALUES (null, 1, 1);


SELECT * FROM 'Moods';
SELECT * FROM 'Entries';
SELECT * FROM Tags;
SELECT * FROM EntryTags;
