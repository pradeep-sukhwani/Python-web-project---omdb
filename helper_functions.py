import omdb # Import imdb module

def organise_movie_info(movie_details):
    # This function return movie details in a organised way
    movie_details_organised = "Title: " + movie_details.title + \
    "<br>IMDB Rating: " + movie_details.imdb_rating + \
    "<br>Released Date: " + movie_details.released + \
    "<br>Actors: " + movie_details.actors + \
    "<br>Language: " + movie_details.language + \
    "<br>Shooting Location: " + movie_details.country + \
    "<br>Genre: " + movie_details.genre + \
    "<br>Writer: "+ movie_details.writer + \
    "<br>Driector: " + movie_details.director + \
    "<br>Poster: " + movie_details.poster + \
    "<br>Run Time: " + movie_details.runtime + \
    "<br>IMDB Votes: " + movie_details.imdb_votes + \
    "<br>Type: " + movie_details.type + \
    "<br>IMDB ID: " + movie_details.imdb_id + \
    "<br>Plot: " + movie_details.plot
    return movie_details_organised

def search_by_title(name):
    # This function return movie details by title
    movie_details = omdb.title(name)
    return organise_movie_info(movie_details)

def search_by_id(name):
    # This function return movie details by IMDI ID
    movie_details = omdb.imdbid(name)
    return organise_movie_info(movie_details)

def main_call(name):
    # This function check whether there is agrument and if it has then
    # is it valid movie name or not.
    if name[0:2] == "tt":
        return search_by_id(name)
    elif name:
        return search_by_title(name)
    else:
        raise Exception('Please enter name')

def escape_html(s):
    # Define functione for html escape
    if s == '>':
      return '&gt;'
    elif s == '<':
      return '&lt;'
    elif s == '"':
      return '&quot;'
    elif s == '&':
      return '&amp;'
    else:
      return s