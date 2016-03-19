require 'httpclient'
require 'uri'
require 'json'

extheaders = {
  'User-Agent' => 'Holberton_School',
  'Authorization' => 'token f4f6caa6a3e5f5da491e42d6ee14708f325ad655'
}

client = HTTPClient.new
uri = URI.parse("https://api.github.com/search/repositories?q=language:ruby&sort=stars&order=desc")
result = client.get(uri, nil, extheaders)
c = JSON.parse(result.content)
c["items"].map{ |arr| puts arr['full_name'] }
