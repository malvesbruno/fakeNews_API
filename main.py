from fastapi import FastAPI
from pydantic import BaseModel
import joblib

app = FastAPI() # cria a API
model = joblib.load('models/fake_news_model.pkl') # Carrega o modelo de ML
vectorizer = joblib.load('models/tfidf_vectorizer.pkl') # carrega o vetorizador

#cria um modelo base para como os dados devem vir para a api
class News(BaseModel): 
    text:str

# Metodo post
# enviamos dados para a api
@app.post('/predict')
def predict(news: News):
    textVectorized = vectorizer.transform([news.text])
    pred = model.predict(textVectorized)[0]
    return {"prediction": int(pred)}

# Metodo get
# Passmos dados através da url querys
@app.get('/predict')
def predict_get(text: str):
    textVectorized = vectorizer.transform([text])
    pred = model.predict(textVectorized)[0]
    return {"prediction": int(pred)}