import pickle
from sklearn.externals import joblib
from nltk.stem import WordNetLemmatizer
import numpy as np
from collections import Counter 
import math  
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

def maxListPosition(cs_array,i):
	maxList = []
	#print(len(maxList))
	while (len(maxList)<(i+1)):
		max_value = cs_array[0]
		max_i = 0
		for x in range(len(cs_array)):
			if max_value<cs_array[x] and x not in maxList:
				max_value = cs_array[x]
				max_i = x
		maxList.append(max_i)

	return maxList


filename = 'DF.sav'
with open(filename, 'rb') as handle:
    DF = pickle.load(handle)
filename = 'tf_idf.sav'
with open(filename, 'rb') as handle:
    tf_idf = pickle.load(handle)
filename = 'total_vocab.sav'
with open(filename, 'rb') as handle:
    total_vocab = pickle.load(handle)
filename = 'D.sav'
D = np.loadtxt(filename,dtype=float)  
filename = 'content.sav'
with open(filename, 'rb') as handle:
    content = pickle.load(handle)  

def search(query,l):
	tokens = preprocessing(query).split(" ")
	Q = np.zeros((len(total_vocab)))
	counter = Counter(tokens)
	words_count = len(tokens)
	query_weights = {}
	for token in np.unique(tokens):
		if token!='':
		    tf = counter[token]/(1.0*words_count)
		    try:
			    df = len(DF[token])
			    idf = math.log((len(content)+1.0)/(df+1.0))
			    Q[total_vocab.index(token)] = tf*idf
		    except:
			    print("EXCEPTION:"+token)

	cosine_similarity = []
	for i in D:
		dot_product = 0.0
		for j in range(len(total_vocab)):
			dot_product = dot_product + i[j] * Q[j]
		dot_product = dot_product/(norm(i)*norm(Q))

		cosine_similarity.append(dot_product)

	max_list = maxListPosition(cosine_similarity,l)
	print(max_list)

	f = open("results.txt", "w")
	for x in max_list:
		f.write(content[x]+"\n")
	f.close()

query = sys.argv[1]
search(query,20)

# print(max(cosine_similarity))
# print(cosine_similarity.index(max(cosine_similarity)))
# print(content[cosine_similarity.index(max(cosine_similarity))])


