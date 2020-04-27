#!/bin/bash
rm out.txt
rm temp.txt

#python change_json.py <Number of files to be returned> <query as required by galago>
python change_json.py 10 "#combine(#bm25(f-script) #bm25(programming) #bm25(language) #bm25(references))"

#<location of the galago exe> batch-search <json file created> >> <output file to be written to>
../galago batch-search bm25-search.json >> temp.txt

# Since batch-search of bm23 returns lots of unrequired information, the required files locations are mentioned in the last few lines which will be taken by last_n.py file from temp.txt

#python last_n.py <Number of files to be returned> >> <And writes to new file>
python last_n.py 10 >> out.txt

#out.txt contains the top n closest files to the query.
#paragraph.py reads the files and converts them into paragraphs. Every paragraph will be in new line. The output is written to numbered_out.txt

#python paragraph.py
python paragraph.py

#corpus_cpy.py searches the numbered_out.txt for the most relevant paragraph, using bm25 module for the query mentioned in args

#python corpus_cpy.py <query> <any words you wish to be compulsorily present in the required passage>
python corpus_cpy.py "F-script programming language" ""

#Examples:
#python change_json.py 10 "#combine(#bm25(f-script) #bm25(programming) #bm25(language) #bm25(history))"
#python change_json.py 10 "#combine:0=0.125:1=0.125:2=0.125:3=0.125:4=0.5(#bm25(prefix) #bm25(hash) #bm25(tree) #bm25(operations) #bm25(lookup))"
#python change_json.py 10 #combine(#bm25(prefix) #bm25(hash) #bm25(tree) #bm25(definition))"
#python change_json.py 10 "#combine(#bm25(lexicographic) #bm25(search) #bm25(tree) #bm25(features))"
#python change_json.py 10 "#combine(#bm25(network) #bm25(operating) #bm25(system) #bm25(definition))"
#python change_json.py 10 "#combine(#bm25(semantic) #bm25(interpretation) #bm25(speech) #bm25(recognition) #bm25(introduction) #bm25(basic) #bm25(principle))"
