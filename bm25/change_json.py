import json
import sys

# with open('bm25-search.json', 'r') as file:
#     data = file.read().replace("\n","")

# data = "{      \"verbose\"   : true,      \"casefold\"  : true,      \"requested\" : 15,      \"index\"     : \"ap89.idx\",      \"K\" : 1.2,      \"b\" : $

# json_data = json.loads(data)
# temp = int(sys.argv[1])
# json_data["requested"] = temp

# with open('bm25-search.json', 'w') as file:
#     json.dump(json_data, file, indent=2)


str = "{\"index\": \"ap89.idx\",\"b\": 0.75,\"verbose\": true,\"requested\": "+sys.argv[1]+",\"K\": 1.2,\"casefold\": true,\"queries\": [ {   \"text\": \""+sys.argv[2]+"\",   \"number\": \"bm25-combine\" }]}"
json_data = json.loads(str)

with open('bm25-search.json', 'w') as file:
    json.dump(json_data, file, indent=2)
