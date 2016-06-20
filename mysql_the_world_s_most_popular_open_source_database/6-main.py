import MySQLdb
import json
from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'

connect = MySQLdb.connect(host="173.246.108.142",
			   user="student",
			   passwd="aLQQLXGQp2rJ4Wy5",
			   db="Project_169",
			   port=3306,
			   )

curse = connect.cursor(MySQLdb.cursors.DictCursor)

@app.route("/tvshows")
@app.route("/tvshows/")
def tvshows():
	return runquery("""
		SELECT TVShow.id, TVShow.name, TVShow.poster
		FROM TVShow
		ORDER BY TVShow.name
	""")


@app.route("/tvshow/<showid>")
@app.route("/tvshow/<showid>/")
def tvshow_id(showid):
	query = """
		SELECT
			TVShow.id,
			TVShow.name,
			TVShow.poster,
			TVShow.overview,
			Network.name
		FROM TVShow
		LEFT JOIN Network ON (TVShow.network_id = Network.id)
		WHERE TVShow.id = """ + showid + """
	"""
	curse.execute(query)
	results = curse.fetchall()[0]
	genre_query = """
		SELECT Genre.name
		FROM TVShow
		RIGHT JOIN TVShowGenre
			ON (TVShow.id = TVShowGenre.tvshow_id)
		RIGHT JOIN Genre
			ON (TVShowGenre.genre_id = Genre.id)
		WHERE TVShow.id = """ + showid + """
	"""
	curse.execute(genre_query)
	genres_dict = curse.fetchall()
	genres_list = [i["name"] for i in genres_dict]

	#string encoding is problematic
	udata = results["overview"].decode("latin-1")
	results["overview"] = udata.encode("utf-8")

	results["genres"] = genres_list
	return json.dumps(results)


@app.route("/tvshow/<showid>/actors")
@app.route("/tvshow/<showid>/actors/")
def actors(showid):
	return runquery("""
		SELECT Actor.name, Actor.id
		FROM TVShow
		LEFT JOIN TVShowActor
			ON (TVShow.id = TVShowActor.tvshow_id)
		LEFT JOIN Actor
			ON (TVShowActor.actor_id = Actor.id)
		WHERE TVShow.id = """ + showid + """
		ORDER BY Actor.name;
	""")


@app.route("/tvshow/<showid>/seasons")
@app.route("/tvshow/<showid>/seasons/")
def seasons(showid):
	return runquery("""
		SELECT Season.id, Season.number
		FROM Season
		WHERE Season.tvshow_id = """ + showid + """
	""")


@app.route("/tvshow/<showid>/season/<seasonid>/episodes")
@app.route("/tvshow/<showid>/season/<seasonid>/episodes/")
def episodes(showid, seasonid):
	return runquery("""
		SELECT Episode.id, Episode.name, Episode.number
		FROM Episode
		WHERE Episode.season_id = """ + seasonid + """
	""")


@app.route("/tvshow/<showid>/season/<seasonid>/episode/<episodeid>")
@app.route("/tvshow/<showid>/season/<seasonid>/episode/<episodeid>/")
def episode(showid, seasonid, episodeid):
	return runquery("""
		SELECT
			Episode.id,
			Episode.name,
			Episode.number,
			Episode.Overview
		FROM Episode
		WHERE Episode.id = """ + episodeid + """
	""")


def runquery(query):
	curse.execute(query)
	results = curse.fetchall()
	return json.dumps(results)


if __name__ == "__main__":
    app.run(port=9898)
