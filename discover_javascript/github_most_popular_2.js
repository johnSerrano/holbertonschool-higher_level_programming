 = require('https');

var options = {
	hostname: 'api.github.com',
	path: '/search/repositories?q=language:javascript&sort=stars&order=desc',
	headers: {
		'User-Agent': 'Holberton_School',
		'Authorization': 'token d2066dda3c6bf142b5b0ac9f789de960d35e4e05',
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
	console.log(typeof jsonString);
	console.log(jsonString);
};

var req = https.request(options, function(res) {
	streamToString(res, cb);
});

req.end();
