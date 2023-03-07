# ==================================== #
#        web-youtube-downloader        #
# ==================================== #

# ------------ import libs ----------- #

# core ↓
from flask import Flask # Flask app 
from flask import render_template # show HTML 
from flask import request # take data from input field 

# ---------- name of the app --------- #

appName = "web-youtube-downloader"  
app = Flask(appName)

# ---------------- run --------------- #

# when a user visits the root URL of the app, Flask will call the home function
@app.route('/') 
def home(): # could be named index() as well 
    return render_template('page.html') # display HTML when viewing URL 

# when a user submits the data in the input field we take it and generate a response
@app.route('/submit', methods=['POST'])
def submit():
    
    # take data from HTML input field and assign to a Python variable 
    url = request.form['url']
    
    # save URL from the input field to .txt file 
    with open('url.txt', 'w') as f:
        f.write(str(url))
    
    # need to return anything so it doesn't crash
    return f'URL is: {url}'

if __name__ == '__main__': # common programming idiom that allows you to specify code that should only be executed if the Python script is run directly as the main program, rather than being imported as a module into another program
    app.run(debug=True) # run app 