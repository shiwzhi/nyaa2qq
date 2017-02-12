import requests
class Coolq(object):
	"""dservertring for Coolq"""
	def __init__(self, server):
		super(Coolq, self).__init__()
		self.server = server

	def send_group_message(self, msg, gid):
		payload = {'group_id': gid, 'message': msg, 'is_raw': True}
		self.send_request("{}/send_group_msg".format(self.server), payload)

	def send_request(self, url, json_payload):
		try:
			r = requests.post(url, json=json_payload)
			print(str(json_payload)+"发送成功")
		except Exception as e:
			print(e)