<<<<<<< HEAD
from flask import Flask, request, redirect

import cgi

app = Flask(__name__)

page_header = """
<!DOCTYPE html>
<html>
    <head>
        <title>FlickList</title>
    </head>
    <body>
        <h1>Flicklist</h1>
"""
page_footer = """
    </body>
</html>
"""

add_form = """
    <form action="/add" method="POST">
        <label for="new-movie">I want to add
        <input type="text" id="new-movie" name="new-movie">
        to my watchlist.
        </label>
        <input type="submit" value="Belly" >
    </form>
"""

current_movies = [
    "Star Wars",
    "My Favorite Martian",
    "The Avengers",
    "The Hitchhikder's Guide To The Galaxy"
]
def get_current_movies():
    crossoff_options = ''
    for movie in current_movies:
        crossoff_options += '<option value="{0}">{0}</option>'.format(movie)
    return current_movies

crossoff_options = ''
for movie in get_current_movies():
    crossoff_options += '<option value="{0}">{0}</option>'.format(movie)

crossoff_form = """
    <form action="/crossoff" method="POST">
        <label>
            I want to cross off
            <select name="crossed-off-movie"/>
                {0}
            </select>
        </label>
        <input type="submit" value="Cross It Off"/>
    </form>
""".format(crossoff_options)

@app.route("/crossoff", methods=['POST'])
def crossoff_movie():
    crossed_off_movie = request.form['crossed-off-movie']

    # Don't allow movies not in the list
    if crossed_off_movie not in get_current_movies():
        error_msg = "'{0}' is not in the watchlist. Have a nice day!".format(crossed_off_movie)
        return redirect('/?error={0}'.format(error_msg))

    crossed_off_movie_element = "<strike>" + crossed_off_movie + "</strike>"
    confirmation = crossed_off_movie_element + " has been crossed off your WatchList."
    content = page_header + "<p>" + confirmation + "</p>" + page_footer

    return content


@app.route('/add', methods=['POST'])
def add_movie():
    new_movie = request.form['new-movie']
    if type(new_movie) is not str or new_movie == '':
        error_msg = "'{0}' is not in a valid movie. Check IMDB".format(new_movie)
        return redirect('/?error={0}'.format(error_msg))

    # build response content
    new_movie_element = "<strong>" + cgi.escape(new_movie) + "</strong>"
    sentence = new_movie_element + " has been added to the watchlist"
    content = page_header + "<p>" + sentence + "</p>" + page_footer

    return content

@app.route("/")
def index():
    edit_header = '<h2>Edit My WatchList</h2>'

    error = request.args.get('error')
    if error:
        esc_error = cgi.escape(error, quote=True)
        error_element = '<p class="error">{0}</p>'.format(esc_error)
    else:
        error_element = ''

    # build the response string
    content = page_header + edit_header + error_element + add_form + crossoff_form + page_footer
    #content = page_header + edit_header + error_element + add_form  + crossoff_form + page_footer
    return content


app.run(debug=True)
=======
from flask import Flask
import random

app = Flask(__name__)

app.config['DEBUG'] = True      # displays runtime errors in the browser, too

@app.route("/")



def index():
    # choose a movie by invoking our new function
    today_movie = get_random_movie()
    tommorrow_movie = get_random_movie()
    while tommorrow_movie == today_movie:
         tommorrow_movie = get_random_movie()


    # build the response string
    content = "<h1>Movie of the Day</h1>"
    content += "<ul>"
    content += "<li>" + today_movie + "</li>"
    content += "</ul>"

    # TODO: pick another random movie, and display it under
    # the heading "<h1>Tommorrow's Movie</h1>"

    content_tom = "<h1>Tommorrow's Movie</h1>"
    content_tom += "<ul>"
    content_tom += "<li>" + tommorrow_movie + "</li>"
    content_tom += "</ul>"

    return content + content_tom

def get_random_movie():
    #TODO: make a list with at least 5 movie titles
    mov_list = ['Bolt','Star Wars','Harry Potter', 'Catch Me If You Can', 'Toy Story']

    #TODO: randomly choose one of the movies, and return it
    #TODO: randomly choose one of the Tommorrow's movie without repeating
    select_mov = random.choice(mov_list)

    return select_mov






app.run()
>>>>>>> 90713471258cb6873a419a5e396a0249d711bafb
