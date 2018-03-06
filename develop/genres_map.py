import csv

def make_genres_map(dict, filepath):
    """Creates a dictionary which maps all movie genres to a unique genre code used in the movies revenue prediction model.

    Args:
        dict: dictionary to store mapping.
        filepath: dataframe containing movie attributes.

    Returns:
        Dictionary containing the genre to code mapping.

    """
    genre_file = open(filepath)
    genre_reader = csv.reader(genre_file)
    next(genre_reader)
    for row in genre_reader:
        dict.update({row[1]:row[0]})
    return dict
