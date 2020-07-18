import imdb

ia= imdb.IMDB()
search = ia.get_top_250_movies()
for i in range(10):
    print(search[i])
