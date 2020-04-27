#!/usr/bin/env python
# coding: utf-8

# In[6]:

import sys
# import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
# from nltk.tokenize import word_tokenize

def load_data_txt(path):
    # f = open(path, 'r',encoding="utf8")
    with open(path) as f:
        content = f.readlines()

    

#    lines = []
#    while True:
#        line = f.readlines()
#        if not line:
#            break
#        lines.append(line.rstrip())
    return content
        


def tf_idf(search_keys, dataframe, label):
  
	tfidf_vectorizer = TfidfVectorizer()
	tfidf_weights_matrix = tfidf_vectorizer.fit_transform(dataframe.loc[:, label])
	search_query_weights = tfidf_vectorizer.transform(search_keys)
	
	return search_query_weights, tfidf_weights_matrix

def cos_similarity(search_query_weights, tfidf_weights_matrix):
	
	cosine_distance = cosine_similarity(search_query_weights, tfidf_weights_matrix)
	similarity_list = cosine_distance[0]
  
	return similarity_list

def most_similar(similarity_list, min_talks=1):
	
	most_similar= []
  
	while min_talks > 0:
		tmp_index = np.argmax(similarity_list)
		most_similar.append(tmp_index)
		similarity_list[tmp_index] = 0
		min_talks -= 1

	return most_similar


# path1 = "D:\\study\\sem 9\\MTP1\\search_engine\\sample_from_wiki.csv"
# path2 = "D:\\study\\sem 9\\MTP1\\search_engine\\data.csv"
# data = load_data_txt(path1)

# a,b = tf_idf( ["the","explain"] ,  data , "text" )
# l = cos_similarity(a, b)
# result = most_similar(l, 10)
# resl = []
# for i in result:
#     resl.append(data.loc[i,"text"])

# result1 = resl[0]
# print(result1)
# result1_words = result1.split()
# for i in result1_words:
#     if i == "explain":
#         print(i)
#     if i == "something":
#         print(i)
    
def word_tokenize(str):
	return str.split()

def compulsory_function(argu,str):
	if len(argu.split(" "))>1:
		for x in argu.split(" "):
			if x in str:
				return True
	else:
		if argu in str:
			return True
	return False

stop_words = ["i","me","my","myself","we","our","ours","ourselves","you","youre","youve","youll","youd","your","yours","yourself","yourselves","he","him","his","himself","she","shes","her","hers","herself","it","its","its","itself","they","them","their","theirs","themselves","what","which","who","whom","this","that","thatll","these","those","am","is","are","was","were","be","been","being","have","has","had","having","do","does","did","doing","a","an","the","and","but","if","or","because","as","until","while","of","at","by","for","with","about","against","between","into","through","during","before","after","above","below","to","from","up","down","in","out","on","off","over","under","again","further","then","once","here","there","when","where","why","how","all","any","both","each","few","more","most","other","some","such","no","nor","not","only","own","same","so","than","too","very","s","t","can","will","just","don","dont","should","shouldve","now","d","ll","m","o","re","ve","y","ain","aren","arent","couldn","couldnt","didn","didnt","doesn","doesnt","hadn","hadnt","hasn","hasnt","haven","havent","isn","isnt","ma","mightn","mightnt","mustn","mustnt","needn","neednt","shan","shant","shouldn","shouldnt","wasn","wasnt","weren","werent","won","wont","wouldn","wouldnt"]

path1 = "numbered_out.txt"
data = load_data_txt(path1)
compulsory = sys.argv[2]


# print(compulsory)

net_tokens = []
for i in range(len(data)):
	if compulsory_function(compulsory,data[i]):
		#print(data.loc[i,'text'])
		net_tokens.append(data[i])

print(len(net_tokens))
print(len(data))

tokens = [(x.split()) for x in net_tokens]
print("tokens length"+str(len(tokens)))
# tokens = [word_tokenize(data.loc[i,'text']) for i in range(len(data))]

for i in range(len(tokens)):
    tokens[i] = [w.lower() for w in tokens[i]]
    
# import string
# table = str.maketrans('', '', string.punctuation)
# stripped = []
# for i in range(len(tokens)):
#     stripped.append([w.translate(table) for w in tokens[i]])
# words = []
# for i in range(len(stripped)):
#     words.append([word for word in stripped[i] if word.isalpha()])

# from nltk.stem.porter import PorterStemmer
# porter = PorterStemmer()
# for i in range(len(words)):
#     words[i] = [porter.stem(w) for w in words[i] if not w in stop_words]
# print(tokens[0][:10])
# print(stripped[0][:10])
# print(words[0][:10])


from rank_bm25 import BM25Okapi

bm25 = BM25Okapi(tokens)
query = sys.argv[1]
#query = "data structure stack implementation"
tokenized_query = query.split(" ")
# tokenized_query = [porter.stem(w) for w in tokenized_query]
print(tokenized_query)
doc_scores = bm25.get_scores(tokenized_query)
results = bm25.get_top_n(tokenized_query, tokens, n=40)
# print(results[0])
indexes = [tokens.index(r) for r in results]
#print(doc_scores)
print(indexes)
#path = "D:\\study\\sem 9\\MTP1\\search_engine\\stack_implementation_linked_list_array.csv"
f = open("results.txt", 'w' ,encoding="utf8")
for i in indexes:
    f.write((" ".join(tokens[i]))+"\n")
f.close()

