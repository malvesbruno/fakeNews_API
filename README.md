# 📰 Fake News Detection API

API REST construída com FastAPI que utiliza um modelo de Machine Learning para classificar notícias como verdadeiras (0) ou falsas (1).
O modelo foi previamente treinado e salvo com joblib, utilizando TF-IDF para vetorização de texto e Logistic Regression para classificação.

## 🚀 Funcionalidades

Classificação de notícias em fake ou real.

Suporte a GET (query params) e POST (JSON body).

Retorno em formato JSON.

## 📂 Estrutura do Projeto

```
├──models/
│   ├── fake_news_model.pkl
│   └── tfidf_vectorizer.pkl
├── main.py                 # Código principal da API
├── requirements.txt        # Dependências do projeto
└── README.md
```

## 🛠️ Tecnologias

- FastAPI
- scikit-learn
- joblib
- Uvicorn

## 📦 Instalação e Execução

Clone o repositório:
```bash
git clone https://github.com/seu-usuario/fake-news-api.git
cd fake-news-api
```
Crie um ambiente virtual e instale as dependências:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
pip install -r requirements.txt
```
Inicie a API:
```bash
uvicorn main:app --reload
```

Acesse a documentação interativa no navegador:
[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

## 🔍 Exemplos de Uso
### 🔹 GET Request
```bash
http://127.0.0.1:8000/predict?text=Essa+noticia+parece+estranha
```

Resposta:
```bash
{"prediction": 1}
```

###🔹 POST Request
```bash
curl -X POST "http://127.0.0.1:8000/predict" \
     -H "Content-Type: application/json" \
     -d '{"text":"Essa notícia parece suspeita..."}'
```

Resposta:
```bash
{"prediction": 0}
```

## 📌 Próximos Passos

 - [ ] Criar Dockerfile para containerizar a API

 - [ ] Subir a aplicação na AWS (ECS, Lambda ou Elastic Beanstalk)

 - [ ] Criar frontend simples que consome a API

## 💡 Esse projeto faz parte de um ecossistema maior:

- [Fake News ML Model](https://github.com/malvesbruno/fakeNews_ml)
 → treinamento do modelo

- [Fake News API](https://github.com/malvesbruno/fakeNews_API)
 → esta API

- [Fake News Frontend](https://github.com/malvesbruno/fakeNews_FrontEnd)
 → interface do usuário
