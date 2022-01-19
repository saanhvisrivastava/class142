import pandas as pd 
import csv

with open('movies.csv',encoding='utf-8') as f:
    reader=csv.reader(f)

    data=list(reader)
    global all_movies
    all_movies=data[1:]

    headers=data[0]

headers.append('poster_link')

#print(len(headers))
with open('final.csv','a+') as f: #append and write mode. add the new data within this file.previous+new
    csvwriter=csv.writer(f)
    csvwriter.writerow(headers)

with open('movie_links.csv',encoding='utf-8') as f:
    global all_movie_links
    reader=csv.reader(f)
    data=list(reader)
    all_movie_links=data[1:]

for movie_item in all_movies:
    poster_found = any(movie_item[7] in movie_link_items for movie_link_items in all_movie_links)
    #print(poster_found)
    if poster_found:
        for movie_link_item in all_movie_links:
            if movie_item[7] == movie_link_item[0]:
                movie_item.append(movie_link_item[1])
                if len(movie_item) == 22:
                    with open("final.csv", "a+",encoding='utf-8') as f:
                        csvwriter = csv.writer(f)
                        csvwriter.writerow(movie_item)


