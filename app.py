from flask import Flask, render_template, url_for,request
import joblib

app = Flask(__name__)

model = joblib.load('SentimentAnalysis.pkl')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict')
def predict():
    return 

@app.route('/output')
def home():
    return render_template('output.html')

if __name__ == '__main__':
    app.run(debug = True)