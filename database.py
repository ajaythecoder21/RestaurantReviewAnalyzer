import psycopg2
import pickle
from flask import request
conn = psycopg2.connect(dbname = "postgres", user = "postgres", password = "G00d@day", host = "localhost")

cur = conn.cursor()

cur.execute("CREATE TABLE res (sentiment VARCHAR);")

file_name = "SentimentAnalysis_Model.pkl"
file_name_2 = 'cv_Model.pkl'
model = pickle.load(open(file_name, 'rb'))
model_2 = pickle.load(open(file_name_2, 'rb'))
text = request.form["box"]
new_data = [text]
vect = model_2.transform(new_data).toarray()
my_pred = model.predict(vect)    
if my_pred == 1:
    ans = "Positive Review"
elif my_pred == 0:
    ans = "Negative Review"
cur.execute("INSERT INTO res (sentiment) VALUES(%s)", (ans))

conn.commit()


conn.close()