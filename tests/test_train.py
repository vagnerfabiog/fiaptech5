import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from unittest.mock import patch
from src import train
import pandas as pd


def test_train_runs_without_error():
    with patch("src.train.load_data") as mock_load:
        # 10 amostras para garantir pelo menos 5 por classe
        df_mock = pd.DataFrame([{
            "job_id": str(i),
            "applicant_id": str(100 + i),
            "status": "contratado" if i % 2 == 0 else "rejeitado",
            "target": 1 if i % 2 == 0 else 0,
            "descricao_vaga": "vaga",
            "requisitos": "requisitos",
            "resumo_candidato": "resumo",
            "titulo": "titulo",
            "tipo_contratacao": "CLT",
            "local_trabalho": "São Paulo",
            "nivel_academico_vaga": "Superior",
            "nivel_ingles_vaga": "Avançado",
            "nivel_espanhol_vaga": "Intermediário",
            "nome": "João",
            "nivel_academico": "Superior",
            "nivel_ingles": "Avançado",
            "nivel_espanhol": "Intermediário"
        } for i in range(10)])

        mock_load.return_value = df_mock
        train.main(cv_folds=2)
