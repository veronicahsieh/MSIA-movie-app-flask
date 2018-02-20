from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/') #root directory, homepage of the website
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/inputdata', methods = ['POST'])
def inputdata():
    if request.method == 'POST':
        genre = request.form['genre']
        year = request.form['release_year']
        runtime = request.form['runtime']
        popularity = request.form['popularity']
        rating = request.form['rating']
        budget = request.form['budget']
        display = 'Genre selected is: ' + genre
        return display

if __name__ == "__main__": #quick check that only run app whenever this app is called directly
    app.run(debug=True) #start this app
