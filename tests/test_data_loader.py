import json
import pandas as pd
from pathlib import Path
import pytest
import src.data_loader as data_loader  # importa o módulo para trocar a variável DATA_DIR

@pytest.fixture(autouse=True)
def tmp_data_dir(tmp_path, monkeypatch):
    # cria estrutura de pastas
    raw = tmp_path / 'data' / 'raw'
    raw.mkdir(parents=True)

    # JSONs mínimos para teste, ajustados conforme seu loader espera
    jobs = {
        "1": {
            "informacoes_basicas": {"titulo_vaga": "Dev"},
            "perfil_vaga": {
                "principais_atividades": "Codar",
                "competencia_tecnicas_e_comportamentais": "Python",
                "local_trabalho": "Remoto",
                "nivel_academico": "Superior",
                "nivel_ingles": "Avançado",
                "nivel_espanhol": "Básico"
            }
        }
    }

    prospects = {
        "1": {
            "prospects": [
                {"codigo": "10", "situacao_candidado": "Contratado"},
                {"codigo": "20", "situacao_candidado": "Rejeitado"}
            ]
        }
    }

    applicants = {
        "10": {
            "formacao_e_idiomas": {
                "nivel_academico": "Superior",
                "nivel_ingles": "Avançado",
                "nivel_espanhol": "Básico"
            },
            "cv_pt": "Experiência em Python",
            "infos_basicas": {"nome": "Alice"}
        },
        "20": {
            "formacao_e_idiomas": {
                "nivel_academico": "Médio",
                "nivel_ingles": "Intermediário",
                "nivel_espanhol": "Básico"
            },
            "cv_pt": "Experiência em Java",
            "infos_basicas": {"nome": "Bob"}
        }
    }

    # Grava os arquivos JSON
    with open(raw / "Jobs.json", 'w', encoding='utf-8') as f:
        json.dump(jobs, f)
    with open(raw / "Prospects.json", 'w', encoding='utf-8') as f:
        json.dump(prospects, f)
    with open(raw / "Applicants.json", 'w', encoding='utf-8') as f:
        json.dump(applicants, f)

    
    monkeypatch.setattr(data_loader, 'DATA_DIR', tmp_path / 'data')

    yield


def test_load_data_columns():
    df = data_loader.load_data()
    assert 'target' in df.columns
    assert set(df['target']) == {1, 0}
    assert 'titulo' in df.columns
    assert 'nome' in df.columns
