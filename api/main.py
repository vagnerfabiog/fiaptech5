import logging
from fastapi import FastAPI, HTTPException
from pydantic import RootModel
import joblib
import pandas as pd
from pathlib import Path

# Configura logging básico
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="Datathon ML API")

# Carrega pipeline treinado (caminho absoluto relativo ao arquivo)
MODEL_PATH = Path(__file__).parent.parent / 'model.joblib'
pipeline = joblib.load(MODEL_PATH)

class Payload(RootModel):
    root: dict

@app.get('/health')
def health():
    return {'status':'ok'}

@app.post('/predict')
def predict(payload: Payload):
    data = payload.root
    df = pd.DataFrame([data])
    try:
        prob = pipeline.predict_proba(df)[:,1][0]
    except Exception as e:
        logger.error(f"Erro na predição: {e}")
        raise HTTPException(status_code=400, detail=str(e))
    return {'score': float(prob)}
