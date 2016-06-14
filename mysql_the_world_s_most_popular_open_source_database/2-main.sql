\! echo "\nNumber of season by TVShow ordered by name (A-Z)?"
SELECT TVShow.name, count(Season.tvshow_id) AS nb_seasons FROM TVShow LEFT JOIN Season ON (TVShow.id = Season.tvshow_id) GROUP BY Season.tvshow_id ORDER BY name;

\! echo "\nList of Network by TVShow ordered by name (A-Z)?"
SELECT TVShow.name AS "TVShow name", Network.name AS "Network name" FROM TVShow LEFT JOIN Network ON (TVShow.network_id = Network.id) ORDER BY TVShow.name;

\! echo "\nList of TVShows ordered by name (A-Z) in the Network 'Fox (US)'?"
SELECT TVShow.name FROM TVShow LEFT JOIN Network ON (TVShow.network_id = Network.id) WHERE Network.name = "FOX (US)" ORDER BY TVShow.name;

\! echo "\nNumber of episodes by TVShows ordered by name (A-Z)?"
SELECT TVShow.name, count(Episode.id) AS nb_episodes FROM TVShow LEFT JOIN Season ON (TVShow.id = Season.tvshow_id) LEFT JOIN Episode ON (Season.id = Episode.season_id) GROUP BY TVShow.id ORDER BY TVShow.name;
