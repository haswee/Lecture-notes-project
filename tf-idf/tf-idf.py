
import re
from nltk.stem import WordNetLemmatizer
import numpy as np
from collections import Counter 
import math  
import pickle
import sys
def lowerCase(str):
	return str.lower()

def removeStopWords(str):
	stop_words = [" ","i","me","my","myself","we","our","ours","ourselves","you","your","yours","yourself","yourselves","he","him","his","himself","she","her","hers","herself","it","its","itself","they","them","their","theirs","themselves","what","which","who","whom","this","that","these","those","am","is","are","was","were","be","been","being","have","has","had","having","do","does","did","doing","a","an","the","and","but","if","or","because","as","until","while","of","at","by","for","with","about","against","between","into","through","during","before","after","above","below","to","from","up","down","in","out","on","off","over","under","again","further","then","once","here","there","when","where","why","how","all","any","both","each","few","more","most","other","some","such","no","nor","not","only","own","same","so","than","too","very","s","t","can","will","just","don","should","now"]
	new_text = ""
	for word in str.split():
	    if word not in stop_words:
	        new_text = new_text + " " + word
	return new_text

def removePunctuation(str):
	#symbols = "!\"#$%&()*+-.,/:;<=>?@[\]^_`{|}~\n"
	symbols = "!\"#$%&*+-.,/:;<=>?@\^_`|~\n"
	new_text = ""
	for x in str.split():
		if x[-1] in symbols:
			new_text = new_text +" "+ x[:-1]
		else:
			new_text = new_text+" "+x
	return new_text.replace("'","")

def removeSingleLetters(str):
	new_text = ""
	for w in str.split():
	    if len(w) > 1:
	       new_text = new_text + " " + w
	return new_text

def lemmization(str):
	lemmatizer = WordNetLemmatizer()
	new_text = ""
	for x in str.split():
		new_text = new_text + " " + lemmatizer.lemmatize(x)
	return new_text

def removeNonAsciiKeys(str):
	#return re.sub(r'[^\x00-\x7F]+',' ', str)
	new_text = ""
	#print("Enetered!")
	for x in str:
		#print(x)
		if ord(x)<128 and ord(x)>31:
			#print(x)
			new_text = new_text+x
	return new_text

def preprocessing(str):
	str = lowerCase(str)
	str = removePunctuation(str)
	str = removeNonAsciiKeys(str)
	#str = removeSingleLetters(str)
	str = lemmization(str)
	str = removeStopWords(str)

	return str.strip()

def norm(vector):
	ans = 0.0
	for x in vector:
		ans = ans + x*x
	return math.sqrt(ans)

dir = sys.argv[1]

#with open("test.txt","r") as file:
with open(dir+"corpus.txt", 'r') as file:
	content = file.readlines()

content = [x.strip() for x in content]
#print(content)
# for x in content:
# 	# print(preprocessing(x))

filename = dir+'content.sav'

with open(filename, 'wb') as handle:
    pickle.dump(content, handle, protocol=pickle.HIGHEST_PROTOCOL)

processed_text = [preprocessing(x) for x in content]

filename = dir+'processed_text.sav'

with open(filename, 'wb') as handle:
    pickle.dump(processed_text, handle, protocol=pickle.HIGHEST_PROTOCOL)


f = open(dir+"corpus_cleaned.txt", "w")
for x in processed_text:
	#f.write(" ".join(x.decode('utf8', 'replace').encode('ascii', 'replace').decode('ascii').split()[1:])+"\n")
	f.write(" ".join(x.split()[1:])+"\n")
	#f.write("\n")
f.close()

print("Corpus_cleaned written!")
"""
DF = {}
for i in range(len(processed_text)):
    tokens = processed_text[i].split(" ")
    # print(tokens)
    for w in tokens:
    	if w !='':
	        try:
	            DF[w].add(i)
	        except:
	            DF[w] = {i}

filename = dir+'DF.sav'
with open(filename, 'wb') as handle:
    pickle.dump(DF, handle, protocol=pickle.HIGHEST_PROTOCOL)

print("DF done!")

tf_idf = {}
print("calculating tf_idf...")

total_vocab = []
for i in range(len(processed_text)):
    tokens = processed_text[i].split(" ")
    counter = Counter(tokens)
    for token in np.unique(tokens):
	#print(i)
    	if token != '':
    		if token not in total_vocab:
    			total_vocab.append(token)

	        if '' in processed_text[i]:
	        	tf = float(counter[token])/float((len(processed_text[i])-(counter[''])))
	        else:
	        	tf = counter[token]/len(processed_text[i])
	        
	        idf = np.log(len(processed_text)+1/(len(DF[token])+1.0))
	        tf_idf[i, token] = (tf)*idf

filename = dir+'tf_idf.sav'
with open(filename, 'wb') as handle:
    pickle.dump(tf_idf, handle, protocol=pickle.HIGHEST_PROTOCOL)

filename = dir+'total_vocab.sav'
with open(filename, 'wb') as handle:
    pickle.dump(total_vocab, handle, protocol=pickle.HIGHEST_PROTOCOL)


print("tf_idf DONE!")

# Document Vectorization
print("Doing: Document vectorization...")
D = np.zeros((len(processed_text), len(total_vocab)))
for i in tf_idf:
    ind = total_vocab.index(i[1])
    D[i[0]][ind] = tf_idf[i]

filename = dir+'D.sav'
np.savetxt(filename, D, fmt='%.3f')

# with open(filename, 'wb') as handle:
#     pickle.dump(D, handle, protocol=pickle.HIGHEST_PROTOCOL)


print("DV done!")

"""
