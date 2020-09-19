import requests
import json

class Client:
	def __init__(self, url, api_key):
		self.url = url
		self.api_key = api_key

	class Application:
		def __init__(self):
			self.headers = {
			  'Accept': 'Application/vnd.pterodactyl.v1+json',
			  'Content-Type': 'application/json',
			  'Authorization': f'Bearer {self.api_key}'
			}

		def _api_request(url, headers=self.headers)
			response = requests.get(url=url, headers=headers)
			return response

		def show_all_servers(self):
			meta_data = _api_request(url=f"{self.url}/api/application/servers")
			response = _api_request(url=f"{self.url}/api/application/servers?page={num}")
			b = []
			for i in range(meta_data['meta']['pagination']['total_pages']):
				b.append(page(i))
			return b
