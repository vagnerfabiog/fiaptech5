from unittest.mock import patch
from src import train

def test_train_runs_without_error():
    with patch("src.train.load_data") as mock_load:
        import pandas as pd
        mock_load.return_value = pd.DataFrame({
            "job_id": ["1"],
            "applicant_id": ["10"],
            "target": [1],
            "descricao_vaga": ["vaga"],
            "requisitos": ["requisitos"],
            "resumo_candidato": ["resumo"],
            "titulo": ["titulo"],
            "tipo_contratacao": ["CLT"],
            "local_trabalho": ["São Paulo"],
            "nivel_academico_vaga": ["Superior"],
            "nivel_ingles_vaga": ["Avançado"],
            "nivel_espanhol_vaga": ["Intermediário"],
            "nome": ["João"],
            "nivel_academico": ["Superior"],
            "nivel_ingles": ["Avançado"],
            "nivel_espanhol": ["Intermediário"]
        })

        train.main()
