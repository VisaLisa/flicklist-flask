from flask import Flask
import random

app = Flask(__name__)

app.config['DEBUG'] = True      # displays runtime errors in the browser, too

@app.route("/")
def index():
    # choose a movie by invoking our new function
    today_movie = get_random_movie()
    tomorrow_movie = get_random_movie()
    while tomorrow_movie == today_movie:
        tomorrow_movie = get_random_movie()

    # build the response string
    content = "<h1>Movie of the Day</h1>"
    content += "<ul>"
    content += "<li>" + today_movie + "</li>"
    content += "</ul>"

    # TODO: pick another random movie, and display it under
    tom_content = "<h1>Tommorrow's Movie</h1>"
    tom_content += "<ul>"
    tom_content += "<li>" + tomorrow_movie + "</li>"
    tom_content += "</ul>"

    return content + tom_content

def get_random_movie():
    # make a list with at least 5 movie titles
    movie_list = ['Get Out', 'Ultraman', 'Harry Potter', 'Big Hero 6', 'Mulan']
    #randomly choose one of the movies, and return it
    select_movie = random.choice(movie_list)

    return select_movie


app.run()
