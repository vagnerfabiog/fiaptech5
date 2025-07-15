import json
import pytest
from fastapi.testclient import TestClient
from api.main import app

client = TestClient(app)

def test_health():
    r = client.get('/health')
    assert r.status_code == 200
    assert r.json() == {'status': 'ok'}


def test_predict_valid_payload():
    payload = {
        "descricao_vaga": "Analista de dados para projetos de BI e visualização.",
        "requisitos": "Power BI, SQL, Python, comunicação com stakeholders.",
        "resumo_candidato": "Trabalhou em BI, controle financeiro e KPIs.",
        "titulo": "Analista de Dados",
        "tipo_contratacao": "CLT",
        "local_trabalho": "São Paulo",
        "nivel_academico_vaga": "Ensino Superior Completo",
        "nivel_ingles_vaga": "Intermediário",
        "nivel_espanhol_vaga": "Nenhum",
        "nome": "Ana Costa",
        "nivel_academico": "Ensino Superior Completo",
        "nivel_ingles": "Intermediário",
        "nivel_espanhol": "Nenhum",
        "recrutador": "Maria Souza",
        "comentario": "Candidato recomendado",
        "nome_x": "Ana Costa",
        "nome_y": "Ana Costa",
        "ultima_atualizacao": "2023-12-01",
        "data_candidatura": "2023-11-28"
    }

    r = client.post('/predict', json=payload)
    assert r.status_code == 200
    assert 'score' in r.json()
    assert 0.0 <= r.json()['score'] <= 1.0
