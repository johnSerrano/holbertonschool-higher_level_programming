import requests

resp = requests.get('https://api.github.com/search/repositories?q=language:python&sort=stars&order=desc', headers={
  'User-Agent': 'Holberton_School',
  'Authorization': 'token f4f6caa6a3e5f5da491e42d6ee14708f325ad655'
})

print resp.json()
