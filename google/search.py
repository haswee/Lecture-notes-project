import urllib
from googlesearch import search 
from bs4 import BeautifulSoup
from tika import parser
import re
import glob

# to search 
query = "F-script programming language"

url_array = search(query, tld="co.in", num=10, stop=5, pause=2)
i=0
html_list = []
pdf_list = []
for j in url_array: 
	print(j)
	split_array =  j.split("/")
	host = split_array[2].split(".")[1]
	if "." in split_array[-1]:
		# pos = split_array[-1].index('.')
		# urllib.request.urlretrieve (j, host+"_"+split_array[-1])
		try:
			urllib.urlretrieve (j, "./dump/"+host+"_"+split_array[-1])
		except:
			print("Failed URL")
		
		pdf_list.append( "./dump/"+host+"_"+split_array[-1])
		print(host+"_"+split_array[-1])
	else:
		# urllib.request.urlretrieve (j, host+"_"+split_array[-1]+".txt")
		try:
			urllib.urlretrieve (j, "./dump/"+host+"_"+split_array[-1]+".txt")
		except:
			print("Failed URL")
		html_list.append( "./dump/"+host+"_"+split_array[-1]+".txt")
		print(host+"_"+split_array[-1]+".txt")
	i=i+1

f = open(query+".txt", "w")

for x in html_list:
	with open(x, 'r') as file:
		data = file.read()
		soup = BeautifulSoup(data, "html.parser")
		out_print = soup.find_all('p')
		# print(out_print)
		file_name = x[[pos for pos, char in enumerate(x) if char == "/"][-1]+1:]
		print(file_name)
		# f = open("./results/"+file_name, "w")
		for y in out_print:
			f.write(y.text.encode('utf-8').replace("\n"," ")+"\n")
			# f.write(y.text.encode('utf-8'))
		# f.close()

for x in pdf_list:
	file_name = x[[pos for pos, char in enumerate(x) if char == "/"][-1]+1:-4]
	if x[-3:]=="pdf":
		# f = open("./results/"+file_name+".txt", "w")
		raw = parser.from_file(x)
		content = raw['content'].encode('utf-8').replace("\n\n","\n")
		prev = ""
		for x in content.split("\n"):
			if not re.match('^[0-9\.\ \-\+]*$',x):
				prev = prev + x.strip()+" "
				stops_list = [pos for pos, char in enumerate(prev) if char == "."]
				if len(stops_list)>3:
					f.write(prev[:stops_list[-1]+1]+"\n")
					prev = prev[stops_list[-1]+1:]
		# f.close()
f.close()
