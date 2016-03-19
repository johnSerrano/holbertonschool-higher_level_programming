require 'httpclient'
require 'uri'

extheaders = {
  'User-Agent' => 'Holberton_School',
  'Authorization' => 'token f4f6caa6a3e5f5da491e42d6ee14708f325ad655'
}

client = HTTPClient.new
url = "https://api.github.com/search/repositories?q=language:ruby&sort=stars&order=desc"
uri = URI.parse(url)
result = client.get(uri, nil, extheaders)
puts result.content
