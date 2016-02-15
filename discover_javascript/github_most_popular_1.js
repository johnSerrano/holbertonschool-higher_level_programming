var https = require('https');

var options = {
	hostname: 'api.github.com',
	path: '/search/repositories?q=language:javascript&sort=stars&order=desc',
	headers: {
		'User-Agent': 'Holberton_School',
		'Authorization': 'token d2066dda3c6bf142b5b0ac9f789de960d35e4e05',
		'Accept': '*/*'
	}
}

var req = https.request(options, function(res) {
	console.log(res.statusCode);
	res.on('data', function(d) {
		process.stdout.write(d);
	});
});
req.end();
