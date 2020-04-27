# Lecture-notes-project

Location of corpus: haswee@aryabhata.cse.iitd.ac.in:/home/haswee/harshrai/galago-3.15-bin/bin_merge/merge/all_text
Galago indexed file location: haswee@aryabhata.cse.iitd.ac.in:/home/haswee/harshrai/galago-3.15-bin/bin_merge/merge/ap89.idx

Download galago search engine and index the corpus. That indexed executable(.galago) is being used everywhere. Please change the location of the .galago accordingly.

## Method-1: BM25 on the whole corpus ##
`bm25-bash.sh` requires various files and their working is explained in the file itself. After running the file, this returns results.txt which contains the most relevant paraghraphs.
> cd bm25

> bash bm25-bash.sh

## Method-2: Improving corpus using Google search results ##
Google search is used to search query, and the links (html and pdf) are downloaded. <p> content of the html files are used, while pdf are converted into text.
`search.py` takes the search query in the file and returns one file <query>.txt which contains paragraphs in each line. For ease, dump folder shows you all the files which are downloaded for the formation of <query>.txt.
> cd google
  
> python search.py
### BM25+New Corpus ###
`bm25-bash.sh` requires various files and their working is explained in the file itself. After running the file, this returns results.txt which contains the most relevant paraghraphs.
> cd bm25

> bash bm25-bash.sh

## Method-3: TF-IDF (Cosine Similarity) ##
For tf-idf, the top-20 files of the corpus and google results are written in `corpus.txt`. 
> cd tf-idf

> python tf-idf.py <directory where corpus.txt is located>

ex: python tf-idf.py "./F/" 

Once the corpus is vectorised, queries can be made using the `query.py`or using the search function of query.py.
> python query.py <query>

ex: python query.py "F-script programming language"

## Method-4: Using GloVe (Cosine Similarity) ##
For glove, the top-40 files of the corpus and google results are written in `corpus.txt`. Install GloVe and run it on the corpus file created, place the output `vectors.txt` in the same directory as the corpus file.
> cd glove

> python glove_vectorization.py <directory where corpus.txt and vectors.txt is located>

ex: python glove_vectorization.py "./F/" 

Once the corpus is vectorised, queries can be made using the `query.py`or using the search function of glove_query.py.
> python glove_query.py <query>

ex: python glove_query.py "F-script programming language"
