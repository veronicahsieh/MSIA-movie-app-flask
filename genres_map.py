import csv

def make_genres_map(dict, filepath):
    genre_file = open(filepath)
    genre_reader = csv.reader(genre_file)
    next(genre_reader)
    for row in genre_reader:
        dict.update({row[1]:row[0]})
    return dict
