\! echo "\nNumber of seasons by tvshow_id?"
SELECT TVShow.id, count(Season.tvshow_id) FROM TVShow LEFT JOIN Season ON (TVShow.id = Season.tvshow_id) GROUP BY Season.tvshow_id;

\! echo "\nNumber of occurrences of the same episode number ordered by episode number?"
SELECT DISTINCT number, COUNT(number) FROM Episode GROUP BY number;

\! echo "\nTop 3 of the Genre's occurrences in all TVShows ordered by this number?"
SELECT genre_id, COUNT(genre_id) FROM TVShowGenre GROUP BY genre_id ORDER BY count(genre_id) DESC limit 3;

\! echo "\nSearch all TVShow with this letter sequence 'th' case insensitive and display with the name in lowercase?"
SELECT LOWER(name) FROM TVShow WHERE name LIKE "%th%";
