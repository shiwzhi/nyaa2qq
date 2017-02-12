import requests
import xml.etree.ElementTree as ET


def get_torrent(fanhao):
	chepai = fanhao

	r = requests.get("https://sukebei.nyaa.se/?page=rss&term={}".format(chepai))

	root = ET.fromstring(r.text)

	channel = root[0]
	url_list = []
	temp_link = ""
	temp_count = ""
	for i in channel.findall("item"):
		temp_link = i.find("link").text
		temp_count = int(i.find("description").text.split(',')[2].split(" download(s)")[0])
		url_list.append(list([temp_count, temp_link]))

	return(sorted(url_list, reverse=True)[0][1])

