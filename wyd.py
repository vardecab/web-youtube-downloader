# ==================================== #
#        web-youtube-downloader        #
# ==================================== #

# ------------ import libs ----------- #

# core ↓
from flask import Flask  # Flask app
from flask import render_template  # show HTML
from flask import request  # take data from input field

# ---------- name of the app --------- #

appName = "web-youtube-downloader"  # overwrite default
app = Flask(appName)  # use the name

# --------------- core --------------- #

# when a user visits the root URL of the app, Flask will call the home function
@app.route('/')
def home():  # could be named index() as well
    return render_template('page.html')  # display HTML when viewing URL

# when a user submits the data in the input field we take it and generate a response
@app.route('/submit', methods=['POST'])
def submit():

    # ---------------- URL --------------- #

    # take data from HTML input field and assign to a Python variable
    url = request.form['url']

    print(f"URL: {url}")  # status

    # save URL from the input field to .txt file
    with open('url.txt', 'w') as f:
        f.write(str(url))  # write URL as string to the file

    # ------------ other stuff ----------- #

    # and now check if we want music or video
    # takes from `name` of the field in HTML not ID; True if checked, else False
    music_checkbox = 'download_music' in request.form
    # takes from `name` of the field in HTML not ID; True if checked, else False
    video_checkbox = 'download_video' in request.form

    # check if user wants a video (check if True (= checkbox ticked))
    if video_checkbox:
        print("Let's download some video.")  # status
        # do some magic
        return f'URL is: {url} and we need video.'
    elif music_checkbox:  # they don't want a video, they want music instead
        print("Let's download just music from that video.")  # status
        # do some other magic
        return f'URL is: {url} and we need music.'
    else:  # nothing checked
        print("Nothing checked...")  # status
        return f'URL is: {url} but nothing was selected.'

# ------------ run the app ----------- #


if __name__ == '__main__':  # common programming idiom that allows you to specify code that should only be executed if the Python script is run directly as the main program, rather than being imported as a module into another program
    # run app in debug mode: auto-reload, error messages etc.
    app.run(debug=True)
    # app.run() # run app

# NOTE: to run the app: `python wyd.py` in Terminal`
# NOTE: test URL: https://www.youtube.com/watch?v=dQw4w9WgXcQ
