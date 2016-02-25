var https = require('https');

var options = {
	hostname: 'api.github.com',
	path: '/search/repositories?q=language:javascript&sort=stars&order=desc',
	headers: {
		'User-Agent': 'Holberton_School',
		'Authorization': 'token f4f6caa6a3e5f5da491e42d6ee14708f325ad655',
		'Accept': '*/*'
	}
}


var req = https.request(options, function(res) {
	res.on('data', function(d) {
		process.stdout.write(d);
	});
});
req.end();
