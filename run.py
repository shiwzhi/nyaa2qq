import coolq
import nyaa
from flask import Flask, request
import requests

coolq_http_server = 'http://localhost:5700'

app = Flask(__name__)

def file_io(link):
	r = requests.get(link)
	binary = r.content
	torrent = {'file': ('1.torrent',binary, 'application/x-bittorrent')}
	io = requests.post('https://file.io?expires=1d', files=torrent)
	return(io.json()['link'])

@app.route("/coolq", methods=['GET', 'POST'])
def message():
	if request.method == 'POST':
		try:
			data = request.get_json()
			print(data)
			msg  = data['message']
			if msg.split(',')[0] == '道路畅通':
				torrent_link = nyaa.get_torrent(msg.split(',')[1])
				io_link = file_io(torrent_link)
				qq = coolq.Coolq(coolq_http_server)
				qq.send_group_message(io_link, data['group_id'])
		except Exception as e:
			raise(e)
	return 'good'


if __name__ == "__main__":
    app.run()