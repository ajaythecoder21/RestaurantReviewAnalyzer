from flask import Flask
from flask import render_template, url_for, request, redirect
#from joblib import load
import pickle
import psycopg2
#from flask_sqlalchemy import SQLAlchemy
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

from flask_sqlalchemy import SQLAlchemy


#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
#app.config['POSTGRES_URI'] = "postgres://mxsbtsux:oICl9XkY6jxOloQJXf6dV7ms-pkKrUQf@suleiman.db.elephantsql.com:5432/mxsbtsux"
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:G00d@day@localhost/postgres'
db = SQLAlchemy(app)
#model = joblib.load('SentimentAnalysis_Model.pkl')
#conn = psycopg2.connect(dbname = "postgres", user = "postgres", password = "G00d@day", host = "localhost")

#cur = conn.cursor()
#from sqlalchemy import create_engine
#connection_url = 'postgresql+psycopg2://user:passowrd@localhost:5432/postgres'
#engine  = create_engine(connection_url)
#conn = psycopg2.connect(POSTGRES_URI)
'''
with conn:
    with conn.cursor() as cursor:
        cursor.execute("CREATE TABLE IF NOT EXISTS Restaurant(message TEXT);")
'''

class Message(db.Model):
    recognition = db.Column(db.Integer, primary_key = True)
    box = db.Column(db.String(200), unique = True, nullable = True)
    def __init__(self, box):
        self.box = box
        #self.recognition = recognition
    
    def __repr__(self):
        return '<Message %r' % self.box
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
        
        message = Message(request.form['box'])
        db.session.add(message)
        db.session.commit()
        text = request.form["box"]
        new_data = [text]
        vect = model_2.transform(new_data).toarray()
        my_pred = model.predict(vect)
    return render_template('output.html', prediction = my_pred)


if __name__ == '__main__':
    app.run(debug = True)
