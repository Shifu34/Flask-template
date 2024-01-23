from flask import Flask,render_template
import aiml 
import getStats


app=Flask(__name__)

@app.route('/') # home page
def hello_world():
    return render_template('index.html')

@app.route('/cars') #different pages
def products():
    return 'This is page of car'

@app.route('/getStats') #different pages
def products():
    return aiml.getStats()


if __name__=="__main__":
    app.run(debug=True)
