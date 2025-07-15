from unittest.mock import patch
from src.train import main

def test_train_runs_without_error():
    with patch("src.data_loader.load_data") as mock_load:
        import pandas as pd
        # Simula um DataFrame vazio ou com dados mínimos
        mock_load.return_value = pd.DataFrame({
            "job_id": ["1"],
            "applicant_id": ["10"],
            "target": [1]
        })
        main()
