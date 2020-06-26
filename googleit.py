from googlesearch import search

query="rohit sharma"

for i in search(query, num=5,stop=5,pause=2):
    print(i)
