# ✅ Projeto Datathon - Machine Learning Engineering

Este projeto tem como objetivo prever a **probabilidade de contratação** de um candidato para uma vaga, utilizando técnicas de machine learning com FastAPI, scikit-learn e Docker. Foi desenvolvido como parte de um desafio da pós-graduação da FIAP.

---

## 🧠 Funcionalidades

- Pré-processamento dos dados de candidatos e vagas.
- Treinamento de modelo com pipeline do scikit-learn.
- Exposição da previsão por meio de uma API FastAPI.
- Testes automatizados com `pytest`.
- CI/CD com GitHub Actions.
- Publicação da API na nuvem com Docker + Render.

---

## 📁 Estrutura do Projeto

```
desafio/
├── api/                 # Código da API FastAPI
├── data/                # Dados brutos (.json)
│   └── raw/
├── models/              # Modelo treinado (model.joblib)
├── notebooks/           # Cadernos Jupyter (exploração opcional)
├── src/                 # Código fonte principal
│   ├── data_loader.py
│   ├── features.py
│   ├── model.py
│   ├── train.py
│   └── predict.py
├── tests/               # Testes automatizados com pytest
├── Dockerfile           # Docker para API
├── docker-compose.yml   # Composição com Docker
├── requirements.txt     # Dependências do projeto
└── README.md            # Este arquivo
```

---

## 🚀 Como Executar Localmente

### 1. Clone o repositório

```bash
git clone https://github.com/seuusuario/desafio-ml.git
cd desafio-ml
```

### 2. Crie o ambiente virtual

```bash
python -m venv .venv
source .venv/bin/activate   # Linux/macOS
.venv\Scripts\activate      # Windows
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Treine o modelo

```bash
python src/train.py
```

> Isso irá gerar o arquivo `models/model.joblib`.

---

## 🔎 Como Testar a API

### 1. Rodar localmente

```bash
uvicorn api.main:app --reload
```

Depois, acesse:

- `http://localhost:8000/docs` → Documentação Swagger
- `http://localhost:8000/health` → Health check

### 2. Fazer uma previsão via curl

```bash
curl -X POST http://localhost:8000/predict   -H "Content-Type: application/json"   -d @tests/test_input.json
```

---

## 🐳 Rodar com Docker Compose

```bash
docker-compose up --build
```

A API ficará acessível localmente em `http://localhost:8000`.

---

## ✅ Rodar Testes

```bash
set PYTHONPATH=.
pytest tests/
```

---

## 🔁 CI/CD com GitHub Actions

O projeto conta com:

- Linting com `flake8`
- Testes automatizados com `pytest`
- Build Docker

Tudo executado automaticamente via workflow `ci.yml` no GitHub Actions.

---

## ☁️ Publicação com Render

A aplicação foi publicada com sucesso na plataforma **Render**:

🔗 **URL pública:** [https://fiaptech5.onrender.com](https://fiaptech5.onrender.com)

📄 **Swagger:** [https://fiaptech5.onrender.com/docs](https://fiaptech5.onrender.com/docs)