\! echo "\nList of all tables?"
SELECT table_name FROM information_schema.tables where table_schema = "Project_169";

\! echo "\nDisplay the table structure of TVShow, Genre and TVShowGenre?"
SHOW CREATE TABLE TVShow;
SHOW CREATE TABLE Genre;
SHOW CREATE TABLE TVShowGenre;

\! echo "\nList of TVShows, only id and name ordered by name (A-Z)?"
SELECT id, name FROM TVShow ORDER BY name;

\! echo "\nList of Genres, only id and name ordered by name (Z-A)?"
SELECT id, name FROM Genre ORDER BY name DESC;

\! echo "\nList of Network, only id and name?"
SELECT id, name FROM Network;

\! echo "\nNumber of episodes in the database?"
SELECT COUNT(id) FROM Episode;
