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
