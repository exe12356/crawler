import requests
import json
import os
import time
import aiohttp
import asyncio

# folder = 'book118'
req = requests.get('https://view45.book118.com/PW/GetPage?f=dXAyNS5ib29rMTE4LmNvbS44MFwzNzY0NDEyLTU5OGI0YTRhMmI4MTUucGRm&img=&isMobile=false&readLimit=H8RIDWKvLg3dHrPArPS1rg==&sn=0&furl=o4j9ZG7fK94ywCJ0aQkdUad3YkM4Kc1@bPc_5q6yqfMcdR5aGeBGGFjkm181QeXxGxWH6Oen2bScE0rIXbRO0rC3eclAly7y8rzyccWPlN0=')
folder = 'book118'

test = 5
data = json.loads(req.text)

PageIndex = data['PageIndex']

NextPage = data['NextPage']
PageCount = data['PageCount']

info = {PageIndex:NextPage}

if not os.path.exists(folder):
	os.mkdir(folder)

for x in range(test):
	url = 'https://view45.book118.com/PW/GetPage?f=dXAyNS5ib29rMTE4LmNvbS44MFwzNzY0NDEyLTU5OGI0YTRhMmI4MTUucGRm&img={}&isMobile=false&readLimit=H8RIDWKvLg3dHrPArPS1rg==&sn={}&furl=o4j9ZG7fK94ywCJ0aQkdUad3YkM4Kc1@bPc_5q6yqfMcdR5aGeBGGFjkm181QeXxGxWH6Oen2bScE0rIXbRO0rC3eclAly7y8rzyccWPlN0='
	url = url.format(NextPage,PageIndex)
	imageUrl = 'https://view45.book118.com/img?img={}&tp='
	imageUrl = imageUrl.format(NextPage)
	print(imageUrl)
	data = json.loads(requests.get(url).text)
	NextPage = data['NextPage']
	PageIndex = data['PageIndex']
	info[PageIndex] = NextPage
print(info)

async def __get_content(link):
	async with aiohttp.ClientSession() as session:
		response = await session.get(link)
		content = await response.read()
		return content
       	
       	
       

async def __download_img(index,page):
	print(len(info))
	imageUrl = 'https://view45.book118.com/img?img={}&tp='
	imageUrl = imageUrl.format(page)
	content = await __get_cntent(imageUrl)
	with open(index+'.jpg','wb') as f:
		f.write(content)
	print('DL ' + index )

def run(info):
	start = time.time()
	for x in range(len(info)):
		tasks = [asyncio.ensure_future(__download_img(x,info[x]))]
		loop - asyncio.get_event_loop()
		loop.run_until_complete(asyncio.wait(tasks))
		end = time.time()
		print('total:%s s' %(end - start))


if __name__ == '__main__':
   run(info)

# class Spider(object):
# 	"""docstring for Spider"""
# 	def __init__(self):
# 		self.folder = 'book118'
# 		if not os.path.exists(folder):
# 			os.mkdir(folder)
# 	async def __get_cntent(self,link):
# 		response = await session.get(link)
# 		content = await response.read()
# 		return content
# 	def __get_img_links(self,NextPage):
# 		url = 'https://view45.book118.com/PW/GetPage'
# 		params = {
# 			'f':'dXAyNS5ib29rMTE4LmNvbS44MFwzNzY0NDEyLTU5OGI0YTRhMmI4MTUucGRm'
# 			'img':NextPage
# 			'isMobile':false
# 			'readLimit':'H8RIDWKvLg3dHrPArPS1rg=='
# 			'sn':0
# 			'furl':'o4j9ZG7fK94ywCJ0aQkdUad3YkM4Kc1@bPc_5q6yqfMcdR5aGeBGGFjkm181QeXxGxWH6Oen2bScE0rIXbRO0rC3eclAly7y8rzyccWPlN0='
# 		}
# 		response - requests.get(url,params = params)
# 		if response.status_code == 200:
# 			data = response.json()
# 			# PageIndex = data['PageIndex']
# 			# NextPage = data['NextPage']
# 			return response.json()
# 		else:
# 			print('failed')
# 	async def __download_img(self,img):
# 		content = await self.__get_cntent(img[1])
# 		with open("./%s/%s.jpg" %(folder,PageIndex), "wb") as code:
#    			code.write(requests.get(imageUrl).content)

# 	def run(self):
# 		start = time.time()	
# 		for x in range(PageCount):
# 			links = self.__get_img_links(x)
