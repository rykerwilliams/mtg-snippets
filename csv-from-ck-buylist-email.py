from bs4 import BeautifulSoup
import csv

soup = BeautifulSoup(open(r"c:\users\rj\Documents\ck-python\Gmail - Sell Order Confirmation #6766880.html"), "html.parser")


# print (soup)
with open('6766880.csv', 'w', newline='') as csvfile:
	listwriter = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
	for item in soup.select('table[class*="orderContents"]'):
		# print(item)

		for row in item.find_all('tr'):
			tempRow = []
			for col in row.find_all('td'):
				tempRow.append(col.text)
			listwriter.writerow(tempRow)


print("This line will be printed.")
