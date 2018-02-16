from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/') #root directory, homepage of the website
def index():
    return render_template('index.html')

if __name__ == "__main__": #quick check that only run app whenever this app is called directly
    app.run(debug=True) #start this app


@app.route('/about')
def about():
    return render_template('about.html')
