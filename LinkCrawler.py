from bs4 import BeautifulSoup
import requests
import re
import time
import sys


def Crawler(seed_url, key_phrase):
	
	visited = []
	depth = 1
	queue = [{'url': seed_url, 'depth': 1}]
	
	while len(queue) != 0 and len(visited) < 400 :
		node = queue.pop(0)
		if node['url'] not in (stored_url['url'] for stored_url in visited):
			visited.append(node)
			with open('Crawled_Files' + '-' +str(key_phrase) + '.txt', 'a') as myfile:
				myfile.write("https://en.wikipedia.org" + node['url'] + '\n')

			#print("https://en.wikipedia.org" + node['url'] + " at depth: " + str(node['depth']))
			if (node['depth'] < 6):
				queue = queue + FetchUrls(node,key_phrase)
	
	return visited
		

def FetchUrls(node,key_phrase):
	
	child_urls=[]
	time.sleep(1)
	current_page = (requests.get("https://en.wikipedia.org" + node['url']).text)
	soup = BeautifulSoup(current_page,'html.parser')
	for url in soup.find_all('a', href = True):
		
		if re.search(':', url['href']) or re.search('#', url['href']) or url['href'].endswith('/Main_Page') :
			continue
		
		if key_phrase == '' and re.search('/wiki', url['href']):
			child_urls.append({'url': url['href'], 'depth': node['depth'] + 1})
		
		if key_phrase != '' and re.search('/wiki', url['href']) and re.search(key_phrase, url['href'],re.IGNORECASE):
			child_urls.append({'url': url['href'], 'depth': node['depth'] + 1})
			
		
	return child_urls
	
if __name__=="__main__":
	
	if len(sys.argv) == 3:
		seed_url = sys.argv[1]
		seed_url = seed_url.replace("https://en.wikipedia.org","")
		key_phrase = sys.argv[2]
		print('Seed Document URL: ', sys.argv[1])
		print('Keyphrase: ', sys.argv[2])
		result = Crawler(seed_url, key_phrase)

	if len(sys.argv) == 2: 
		seed_url = sys.argv[1]
		seed_url = seed_url.replace("https://en.wikipedia.org","")
		key_phrase = ''
		print('Seed Document URL: ', sys.argv[1])
		print('No Keyphrase Given')
		result = Crawler(seed_url, key_phrase)
		
	
	
