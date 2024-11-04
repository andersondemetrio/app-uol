# FastAPI File Upload Project

![FastAPI](https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png)

Um projeto robusto em FastAPI para processamento de arquivos CSV e gerenciamento de dados de usuários.

## 📋 Visão Geral

Este projeto demonstra como criar uma API RESTful eficiente utilizando FastAPI. A API oferece funcionalidades para:
- Upload e processamento de arquivos CSV
- Gerenciamento de dados de usuários
- Consultas personalizadas e ordenação
- Sistema de caixa de entrada

## 🚀 Funcionalidades Principais

### 📤 Upload de Arquivos
- Suporte para arquivos CSV
- Validação de nomes de arquivo
- Armazenamento seguro em diretório temporário

### 🔄 Processamento de Dados
- Scripts otimizados para processamento CSV
- Extração e análise de dados de usuários
- Respostas estruturadas com informações detalhadas

### 🔍 Consultas Avançadas
- Ordenação de usuários (asc/desc)
- Filtros por nome
- Sistema de caixa de entrada com contagem de mensagens

## 🛠️ Tecnologias Utilizadas

- FastAPI
- Python 3.8+
- Uvicorn
- Pydantic
- Docker

## ⚙️ Pré-requisitos

- Python 3.8+
- Git
- Docker (opcional)
- Editor de código

## 🔧 Instalação

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/projeto-fastapi.git
cd projeto-fastapi
```

2. Crie e ative o ambiente virtual:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
.\venv\Scripts\activate  # Windows
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Inicie o servidor:
```bash
uvicorn main:app --reload
```

5. Acesse a API em: http://localhost:8000/docs

## 📖 Documentação

A documentação interativa está disponível em:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## 🐳 Docker

### Construindo a imagem:
```dockerfile
FROM python:3.9

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . .
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### Executando com Docker:
```bash
docker build -t fastapi-app .
docker run -p 8000:8000 fastapi-app
```

## 🧪 Testes

Execute os testes com:
```bash
pytest tests/
```

## 👥 Contribuição

1. Fork o projeto
2. Crie sua Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit suas alterações (`git commit -m 'Add some AmazingFeature'`)
4. Push para a Branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 📫 Contato

Seu Nome - [@seuTwitter](https://www.linkedin.com/) - https://www.linkedin.com/in/andersondemetrio/

Link do Projeto: (https://github.com/andersondemetrio/app-uol)
