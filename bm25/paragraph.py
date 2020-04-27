# f = open("test.txt", "r")
# content_file = f.read().split("\n\n")
# prev = ""
# for x in content_file:
# 	x = x.replace("\n","")
# 	prev = prev + x
# 	list_x = [pos for pos, char in enumerate(prev) if char == "."]
# 	if len(list_x)>5:
# 		print(prev)
# 		print('------')
# 		prev = ""		

# print(prev)
# 	# print('------')
# # print(content_file)
import sys
with open('out.txt') as f:
	content = f.readlines()

content = [x.strip() for x in content] 
f_out = open("numbered_out.txt", "w")
i=1

for line in content:
		line_array = line.split(" ")
		rep = [pos for pos, char in enumerate(line_array[2]) if char == "/"]
		num = int(rep[-1])
		pat = "all_text"+line_array[2][num:]
		print(pat)

		if "pdf" in pat:
			f = open(pat, "r")
			content_file = f.read().split("\n\n")
			prev = ""
			for x in content_file:
				x = x.replace("\n","")
				prev = prev + x
				list_x = [pos for pos, char in enumerate(prev) if char == "."]
				if len(list_x)>5:
					f_out.write(str(i)+"\t"+str(prev)+"\n")
					#f_out.write(str(i)+"\t"+str(prev+"\t"+pat+"\n"))
					i=i+1
					# print(prev)
					prev = ""		
			f_out.write(str(i)+"\t"+str(prev.replace("\n","")+"\n"))
			#f_out.write(str(i)+"\t"+str(prev.replace("\n","")+"\t"+pat+"\n"))
		else:
			with open(pat) as f_in:
				lines = f_in.readlines()
			lines = [x.strip() for x in lines] 
			for l in lines:
				if len(l.strip())>0:
					f_out.write(str(i)+"\t"+str(l.strip()+"\n"))
					#f_out.write(str(i)+"\t"+str(l.strip()+"\t"+pat+"\n"))
					i=i+1


#f_out.close()
print(i)
file_name = sys.argv[1]
#with open(file_name+'.txt') as f:
#	content = f.readlines()

file1 = open(file_name+'.txt', 'r') 
content = file1.readlines() 


#content = [x.strip().replace("\n","") for x in content] 
#content = content_read.split("\n")
for line in content:
	if line.strip()=="":
		pass
	else:
		f_out.write(str(i)+"\t"+line.strip()+"\n")
		i=i+1


f_out.close()
print(i)
