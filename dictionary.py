from urllib2 import urlopen, HTTPError, URLError
from bs4 import BeautifulSoup

try:
	page_num = input("What page would you like to look at?  ")
	html = urlopen("https://www.lambgoat.com/mb/?page={}".format(page_num))
except HTTPError as e:
	print(e)
except URLError:
	print("POOTERS BROKEN")
else:
	res = BeautifulSoup(html, "html.parser")
	tags = res.findAll("span", {"class":"mbs"})
	if res.title is None:
		print("Tag not found, yo")
	else:
		for tag in tags:
			print(tag.getText())