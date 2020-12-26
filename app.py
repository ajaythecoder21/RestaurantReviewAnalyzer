from flask import Flask
from flask import render_template, url_for, request
#from joblib import load
import pickle
#from sklearn.model_selection import train_test_split
#from sklearn.naive_bayes import MultinomialNB
#from sklearn.metrics import classification_report
#from sklearn.externals import joblib
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer()
file_name = "SentimentAnalysis_Model.pkl"
file_name_2 = 'cv_Model.pkl'
model = pickle.load(open(file_name, 'rb'))
model_2 = pickle.load(open(file_name_2, 'rb'))
app = Flask(__name__)

#model = joblib.load('SentimentAnalysis_Model.pkl')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict',methods = ["POST"])
def predict():
    #text = request.get_data("box")
    #model_2.fit_transform(text)
    #converted_text = cv.fit_transform(text)
    #ans = model.predict(converted_text)
    if request.method == "POST":
        text = request.form["box"]
        new_data = [text]
        vect = model_2.transform(new_data).toarray()
        my_pred = model.predict(vect)    
    return render_template('output.html', prediction = my_pred)
#@app.route('/output')
#def output():
    #return render_template('output.html')

if __name__ == '__main__':
    app.run(debug = True)
