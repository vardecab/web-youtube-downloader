# ==================================== #
#        web-youtube-downloader        #
# ==================================== #

# NOTE: can be hosted on PythonAnywhere - everything works

# ------------ import libs ----------- #

# Flask core ↓
from flask import Flask  # Flask app
from flask import render_template  # show HTML
from flask import request  # take data from input field

import os
import tempfile 
import yt_dlp # download YouTube videos 
from flask import send_file # let user download the file to their machine

# ---------- name of the app --------- #

appName = "web-youtube-downloader"  # overwrite default
app = Flask(appName)  # use the name

# ------------- functions ------------ #

def downloadVideo(videoURL): 
    # set options for downloading the file
    optionalParameters = { 
        'outtmpl': os.path.join(tempfile.gettempdir(), '%(title)s.%(ext)s'),
        'format': 'bestvideo[height<=1080][ext=mp4]+bestaudio[ext=m4a]/mp4',
        'external_downloader': 'aria2c',
        'external_downloader_args': ['-x', '16', '-s', '16', '-k', '100M'],
        'quiet': True, 
        'sponsorblock_remove': True,
        'postprocessors': [{
            'key': 'SponsorBlock',
            'categories': ['sponsor', 'selfpromo', 'interaction'] # segments that have to be removed
        }, {
            'key': 'ModifyChapters',
            'remove_sponsor_segments': ['sponsor', 'selfpromo', 'interaction'] # segments that have to be removed
        }]
    }
    
    # download the file
    with yt_dlp.YoutubeDL(optionalParameters) as ydl:
        info_dict = ydl.extract_info(videoURL, download=True)
        file_path = ydl.prepare_filename(info_dict)
    
    # send the file for download to the user's browser
    return send_file(file_path, as_attachment=True)

def downloadMusic(videoURL): 
    # set options for downloading the file
    optionalParameters = { 
        # 'outtmpl': os.path.join(tempfile.gettempdir(), '%(title)s.%(ext)s'),
        'outtmpl': os.path.join(tempfile.gettempdir(), '%(title)s.mp3'),
        'quiet': True, # don't throw status messages in the console

        # FIX: produces low-quality files
        "format": "bestaudio/best",
        # "outtmpl": "audio.mp3",
        "extractaudio": True, # music
        "audioquality": "320k", # 320 kbps 
        "audioformat": "mp3",
        
        "noplaylist": True,
        # "add-metadata": True
    }
    
    # download the file
    with yt_dlp.YoutubeDL(optionalParameters) as ydl:
        info_dict = ydl.extract_info(videoURL, download=True)
        file_path = ydl.prepare_filename(info_dict)
    
    # send the file for download to the user's browser
    return send_file(file_path, as_attachment=True)

# --------------- core --------------- #

# when a user visits the root URL of the app, Flask will call the home function
@app.route('/')
def home():  # could be named index() as well
    return render_template('page.html')  # display HTML when viewing URL

# when a user submits the data in the input field we take it and generate a response, ie. download the file
@app.route('/submit', methods=['POST'])
def submit():

    # ---------------- URL --------------- #

    # take data from HTML input field and assign to a Python variable
    videoURL = request.form['videoURL'].strip() # get URL from input field without whitespaces 

    print(f"URL: {videoURL}")  # status

    # save URL from the input field to .txt file
    with open('videoURL.txt', 'w') as f:
        f.write(str(videoURL))  # write URL as string to the file

    # ------------ other stuff ----------- #

    # and now check if we want music or video
    # takes from `name` of the field in HTML not ID; True if checked, else False
    musicButton = 'downloadMusic' in request.form
    # takes from `name` of the field in HTML not ID; True if checked, else False
    videoButton = 'downloadVideo' in request.form

    # check if user wants a video (check if True (= radio button selected))
    if videoButton:
        print("Let's download some video.")  # status
        return downloadVideo(videoURL)
    elif musicButton:  # they don't want a video, they want music instead
        print("Let's download just music from that video.")  # status
        return downloadMusic(videoURL)
    else:  # nothing checked
        print("Nothing checked...")  # status
        return f'URL is: {videoURL} but nothing was selected.'
    
# ------------ run the app ----------- #

os.environ['FLASK_ENV'] = 'production' # run app in production mode

# if __name__ == '__main__':  # common programming idiom that allows you to specify code that should only be executed if the Python script is run directly as the main program, rather than being imported as a module into another program
    # app.run(debug=True) # run app in debug mode: auto-reload, error messages etc.
    # app.run() # run app 

# NOTE: to run the app: `python wyd.py` in Terminal`
# NOTE: test URL: https://www.youtube.com/watch?v=dQw4w9WgXcQ