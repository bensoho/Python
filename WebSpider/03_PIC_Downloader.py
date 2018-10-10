# -*- coding:UTF-8 -*-
import requests,json,time,sys
from contextlib import closing

class get_photos(object):
	"""docstring for get_photos"""
	def __init__(self):
		self.photos_id = []
		self.download_server = 'https://unsplash.com/photos/xxx/download?force=true'
		self.target = 'https://unsplash.com/napi/photos'
		self.headers = {'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}


	def get_download_server(self):
		req = requests.get(url=self.target,headers=self.headers,verify=True)
		html = json.loads(req.text)

		for id in html:
			print('id:',id['id'])
			self.photos_id.append(id['id'])
			time.sleep(1)

	def download(self,photo_id,filename):
		target = self.download_server.replace('xxx',photo_id)
		with closing(requests.get(url=target,stream=True,verify=True,headers=self.headers)) as r:
			with open('%d.jpg' % filename,'ab+') as f:
				for chunk in r.iter_content(chunk_size=1024):
					if chunk:
						f.write(chunk)
						f.flush()

if __name__ == "__main__":
	dl = get_photos()
	dl.get_download_server()
	for i in range(len(dl.photos_id)):
		print(' now downloading photo No#%d' % (i+1))
		dl.download(dl.photos_id[i],(i+1))
