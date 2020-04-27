import sys
with open('temp.txt') as f:
	content = f.readlines()
content = [x.strip() for x in content] 

n = int(sys.argv[1])

for x in range(len(content)-n,len(content)):
	print(content[x])