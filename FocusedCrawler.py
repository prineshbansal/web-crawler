# Submitted by Prinesh Bansal

from bs4 import BeautifulSoup
import requests
import re
import time
import sys


def Crawler(seed_url, key_phrase):
	
	crawled_urls = []
	queue = [{'url': seed_url, 'depth': 1}]
	
	while len(queue) != 0 and len(crawled_urls) < 1000:
		removed_url = queue.pop(0)
		if removed_url['url'] not in (crawled_url['url'] for crawled_url in crawled_urls):
			crawled_urls.append(removed_url)
			print("https://en.wikipedia.org" + removed_url['url'])
			if (removed_url['depth'] < 6):
				queue = queue + FetchUrls(removed_url,key_phrase)
	
	return crawled_urls
		

def FetchUrls(removed_url,key_phrase):
	
	child_urls=[]
	time.sleep(1)
	current_page = (requests.get("https://en.wikipedia.org" + removed_url['url']).text)
	soup = BeautifulSoup(current_page,'html.parser')
	for url in soup.find_all('a', href = True):
		
		if re.search(':', url['href']) or re.search('#', url['href']) or url['href'].endswith('/Main_Page') :
			continue
		
		if key_phrase == '' and re.search('/wiki', url['href']):
			child_urls.append({'url': url['href'], 'depth': removed_url['depth'] + 1})
		
		if key_phrase != '' and re.search('/wiki', url['href']):
			check_page = (requests.get("https://en.wikipedia.org" + url['href']).text)
			if key_phrase in check_page:
				child_urls.append({'url': url['href'], 'depth': removed_url['depth'] + 1})
			
		
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
		
	
	
