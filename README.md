# Lecture-notes-project

Location of corpus: haswee@aryabhata.cse.iitd.ac.in:/home/haswee/harshrai/galago-3.15-bin/bin_merge/merge/all_text
Galago indexed file location: haswee@aryabhata.cse.iitd.ac.in:/home/haswee/harshrai/galago-3.15-bin/bin_merge/merge/ap89.idx

Download galago search engine and index the corpus. That indexed executable(.galago) is being used everywhere. Please change the location of the .galago accordingly.

Method-1: BM25 on the whole corpus
bm25-bash.sh requires various files and their working is explained in the file itself. After running the file, this returns results.txt which contains the most relevant paraghraphs.
> bash bm25-bash.sh
