import requests

resp = requests.get('https://api.github.com/search/repositories?q=language:python&sort=stars&order=desc', headers={
  'User-Agent': 'Holberton_School',
  'Authorization': 'token f4f6caa6a3e5f5da491e42d6ee14708f325ad655'
})

projects = [{
    'owner': i['owner']['login'],
    'full_name': i['full_name']
} for i in resp.json()['items']]

for project in projects:
    url = "https://api.github.com/users/" + project['owner']
    locresp = requests.get(url, headers={
      'User-Agent': 'Holberton_School',
      'Authorization': 'token f4f6caa6a3e5f5da491e42d6ee14708f325ad655'
    })
    project['location'] = locresp.json()['location']

print [{
    'full_name': str(p['full_name']),
    'location': str(p['location'])
} for p in projects]
