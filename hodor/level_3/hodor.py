import urllib, urllib2, cookielib

ID = 1

PHPSESSID_cookie = ""
HoldTheDoor_cookie = ""

cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
resp = opener.open('http://173.246.108.142/level3.php')
for cookie in cj:
	if cookie.name == "PHPSESSID":
		PHPSESSID_cookie = cookie.value
	elif cookie.name == "HoldTheDoor":
		HoldTheDoor_cookie = cookie.value

img = opener.open('http://173.246.108.142/captcha.php')

# write captcha to file
with open('captcha.png', 'w') as imgfile:
	imgfile.write(img.read())

# parse resp for key
for line in resp.readlines():
	if 'key' in line:
		key = line.split('value="')[1]
		key = key.split('" />')[0]

print key

# figure out captcha somehow
captcha = raw_input("Capthca?")

curl = """
curl 'http://173.246.108.142/level3.php' --data 'id=""" + str(ID) + """&key=""" + str(key) + """&captcha=""" + str(captcha) + """&holdthedoor=Submit' -H 'Cookie: PHPSESSID=""" + str(PHPSESSID_cookie) + """; HoldTheDoor=""" + str(HoldTheDoor_cookie) + """' -H 'Referer: http://173.246.108.142/level3.php' -H 'User-Agent: Mozilla/5.0 (Windows NT 6.1; rv:6.0) Gecko/20110814 Firefox/10.0.1' -H 'Origin: http://173.246.108.142'  --compressed
"""

print curl
# run curl command


#curl 'http://173.246.108.142/captcha.php'
# -H 'User-Agent: Mozilla/5.0 (Windows NT 6.1; rv:6.0) Gecko/20110814 Firefox/10.0.1'
# -H 'Cookie: PHPSESSID=31mvmmropeesjfj4lveu5hdts6; HoldTheDoor=8ef9f6b270e032decfd49adc22ee61db60c88afc'



# vote curl
# curl 'http://173.246.108.142/level3.php'
# -H 'Cookie: PHPSESSID=31mvmmropeesjfj4lveu5hdts6; HoldTheDoor=c883dadc20bac38000cd4b2137897111f58fee1c'
# -H 'Origin: http://173.246.108.142'
# -H 'User-Agent: Mozilla/5.0 (Windows NT 6.1; rv:6.0) Gecko/20110814 Firefox/10.0.1'
# --data 'id=1&key=c883dadc20bac38000cd4b2137897111f58fee1c&captcha=69a4&holdthedoor=Submit'
# --compressed
