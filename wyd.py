# ==================================== #
#        web-youtube-downloader        #
# ==================================== #

# ------------ import libs ----------- #

# core ↓
from flask import Flask # Flask app 
from flask import render_template # show HTML 

# ---------- name of the app --------- #

appName = "web-youtube-downloader"  
app = Flask(appName)

# ---------------- run --------------- #

# when a user visits the root URL of the app, Flask will call the home function
@app.route('/') 
def home():
    return render_template('page.html') # display HTML when viewing URL 

if __name__ == '__main__': # common programming idiom that allows you to specify code that should only be executed if the Python script is run directly as the main program, rather than being imported as a module into another program
    app.run(debug=True) # run app 