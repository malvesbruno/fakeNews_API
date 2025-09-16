# 1 - Imagem base do python
FROM python:3.11-slim

# 2 - Diretório de trabalho dentro do container
WORKDIR /app

# 3 - Copiar arquivos de requisitos
COPY requirements.txt .

# 4 - Instalar dependências
RUN pip install --no-cache-dir -r requirements.txt

# 5 - Copiar todo o código da API e modelos
COPY . .

# 6 - Expor a porta que o Uvicorn vai rodar
EXPOSE 8000

# 7 - Comando para rodar a API
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
