from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import joblib

app = FastAPI()

# Adiciona CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # coloca o domínio do seu front se quiser restringir
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Carrega modelo e vetorizador
model = joblib.load('models/fake_news_model.pkl')
vectorizer = joblib.load('models/tfidf_vectorizer.pkl')

# Define estrutura dos dados
class News(BaseModel):
    text: str

# Método POST
@app.post('/predict')
def predict(news: News):
    textVectorized = vectorizer.transform([news.text])
    pred = model.predict(textVectorized)[0]
    return {"prediction": int(pred)}

# Método GET
@app.get('/predict')
def predict_get(text: str):
    textVectorized = vectorizer.transform([text])
    pred = model.predict(textVectorized)[0]
    return {"prediction": int(pred)}
