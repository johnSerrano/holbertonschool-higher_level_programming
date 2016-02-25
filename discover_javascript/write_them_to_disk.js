var https = require('https');
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


function cb(j_string) {
	var jsonString = j_string;
	var file = "/tmp/24";
	fs.writeFile(file, jsonString);
	console.log("The file was saved!");
};

var req = https.request(options, function(res) {
	streamToString(res, cb);
});

req.end();
