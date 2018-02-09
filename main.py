from flask import Flask, request

app = Flask(__name__)

@app.route('/') #root directory, homepage of the website
def index():
    return 'this is the homepage'

if __name__ == "__main__": #quick check that only run app whenever this app is called directly
    app.run(debug=True) #start this app


@app.route('/cluster/<genre>')
def cluster(genre):

@app.route('/about', method = ['GET','POST']) # this page can handle get and post requests
def about():
    if request.method == 'POST':
        return 'you are using POST'
    else:
        return 'you are probably using GET'
