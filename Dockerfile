# Inicializa uma imagem base do Python
FROM python:3.9

# Define o diretório de trabalho
WORKDIR /code

# Copia todos os arquivos do projeto para o container
COPY . .

# Instala as dependências
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Instala python-multipart
RUN pip install python-multipart

# Define o comando para executar a aplicação
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

