import urlparse
import urllib
from bs4 import BeautifulSoup

def writeToFile(dataLine):
	f = open('db.txt','a')
	for item in dataLine:
		f.write(item+'\t') 
	f.write('\n')
	f.close() 
	return


def removeTag(item):
	temp1 = str(item).replace("<h1>", "")
	temp2 = temp1.replace("</h1>", "")
	temp3 = temp2.replace("<span>", "")
	temp4 = temp3.replace("</span>", "")
	temp5 = temp4.replace('<p class="print-pub-date">', "")
	temp6 = temp5.replace("</p>", "")
	temp7 = temp6.replace('<p class="online-pub-date">', "")
	temp8 = temp7.strip()
	return temp8

def readFromFile():
	f = open('isbn.txt','r')
	items = []
	for line in f:
		items.append(line.strip())
	return items
	
myList = readFromFile()

for isbn in myList:

		httpAddress = "http://ebooks.cambridge.org/ebook.jsf?bid=CBO"
		url = httpAddress + str(isbn)

		htmltext = urllib.urlopen(url).read()

		soup = BeautifulSoup(htmltext)

		title = soup.find_all("h1")
		pubDate = soup.find_all("p", {"class" : "print-pub-date" })
		onlinePubDate = soup.find_all("p", {"class" : "online-pub-date" })

		dataLine = [];
		dataLine.append(str(isbn));

		print "+++++++++++++++++++++++"
		for item in title:	
			myTitle = removeTag(item)
			dataLine.append(myTitle)
			print myTitle
			
		print "+++++++++++++++++++++++"
		for item in pubDate:
			myDate = removeTag(item)
			dataLine.append(myDate)
			print myDate
			
		print "+++++++++++++++++++++++"
		for item in onlinePubDate:
			myOnlineDate = removeTag(item)
			if myOnlineDate:
				dataLine.append(myOnlineDate)
				print myOnlineDate

		print "+++++++++++++++++++++++"
		print dataLine

		writeToFile(dataLine);	
