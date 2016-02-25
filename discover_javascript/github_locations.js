var https = require('https');
var request = require("request");
var fs = require('fs');

var options = {
	hostname: 'api.github.com',
	path: '/search/repositories?q=language:javascript&sort=stars&order=desc',
	headers: {
		'User-Agent': 'Holberton_School',
		'Authorization': 'token f4f6caa6a3e5f5da491e42d6ee14708f325ad655',
		'Accept': '*/*'
	}
}

function streamToString(stream, cb) {
	const chunks = [];
	stream.on('data', (chunk) => {
		chunks.push(chunk);
	});
	stream.on('end', () => {
		cb(chunks.join(''));
	});
};


var get_location = (item) => {
	var name = json_copy['items'][item]['owner']['login'];

	var options_for_location = {
		hostname: 'api.github.com',
		path: '/users/' + name,
		headers: {
			'User-Agent': 'Holberton_School',
			'Authorization': 'token f4f6caa6a3e5f5da491e42d6ee14708f325ad655',
			'Accept': '*/*'
		}
	}

	var location_req = (options_for_location, item) => { return https.request(options_for_location, function(res) {
		streamToString(res, (str) => {
		json_copy['items'][item]["location"] = JSON.parse(str)['location'];
                             update_json(item, JSON.parse(str)['location']);
                             console.log(JSON.parse(str)["location"]);
                             console.log(json_copy['items'][item]);
		})
	})};
	var lr = location_req(options_for_location, item);
	lr.end();

};


function cb(j_string) {
	var jsonString = j_string;
	var json_data = JSON.parse(jsonString);
	var json_copy = JSON.parse(jsonString);

//	function update_json(item, local) {
//		json_copy["items"][item]["location"] = local;
//	}
	for (var item in json_data['items']) {
		var local = get_location(item);
		console.log(local);
	}
	console.log(item);
	json_copy['items'][0]["location"] = "asdf";
//	console.log(json_copy);
};

var req = https.request(options, function(res) {
	streamToString(res, cb);
});

req.end();
