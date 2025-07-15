import json
import pandas as pd
from pathlib import Path
import pytest
from src.data_loader import load_data, DATA_DIR

@pytest.fixture(autouse=True)
def tmp_data_dir(tmp_path, monkeypatch):
    # cria estrutura de pastas
    raw = tmp_path / 'data' / 'raw'
    raw.mkdir(parents=True)
    # JSON mínimo
    jobs = {"1": {"descricao_vaga":"dev"}}
    prospects = {"1": {"código_candidato":["10","20"],"situação":["Contratado","Rejeitado"]}}
    applicants = {"10": {"resumo_candidato":"abc"}, "20": {"resumo_candidato":"xyz"}}
    for name, obj in [('Jobs',jobs),('Prospects',prospects),('Applicants',applicants)]:
        with open(raw / f"{name}.json", 'w') as f:
            json.dump(obj, f)
    monkeypatch.setattr(DATA_DIR, 'parent', tmp_path)
    yield


def test_load_data_columns():
    df = load_data()
    assert 'target' in df.columns
    assert set(df['target']) == {1,0}