from flask import Flask
from flask import render_template, url_for, request
#from joblib import load
import pickle
#from sklearn.model_selection import train_test_split
#from sklearn.naive_bayes import MultinomialNB
#from sklearn.metrics import classification_report
#from sklearn.externals import joblib

file_name = "SentimentAnalysis_Model.pkl"
model = pickle.load(open(file_name, 'rb'))

app = Flask(__name__)

#model = joblib.load('SentimentAnalysis_Model.pkl')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict')
def predict():
    text = request.get.args("form_a")
    #return

@app.route('/output')
def output():
    return render_template('output.html')

if __name__ == '__main__':
    app.run(debug = True)
