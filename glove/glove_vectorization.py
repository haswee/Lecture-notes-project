from sklearn.externals import joblib
import sys
import numpy as np

dir = sys.argv[1]
with open(dir+"vectors.txt", 'r') as file:
	content = file.readlines()

content = [x.strip() for x in content]

vectors = {}
for line in content:
	split_array = line.split()
	vectors[split_array[0]] = [float(numeric_string) for numeric_string in split_array[1:]]

filename = dir+'processed_text.sav'
processed_text = joblib.load(filename)

# Document Vectorization
print("Doing: Document vectorization...")
D = np.zeros((len(processed_text), len(vectors[0])))
for i in range(len(processed_text)):
	for j in processed_text[i].split():
		for k in range(len(vectors[0])):
			D[i][k] = D[i][k] + vectors[j][k]

filename = dir+'D_glove.sav'
joblib.dump(D, filename)  
filename = dir+'vectors_glove.sav'
joblib.dump(vectors, filename)  
