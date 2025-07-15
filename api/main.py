import logging
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import pandas as pd

# Configura logging básico
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="Datathon ML API")

# Carrega pipeline treinado
pipeline = joblib.load('../model.joblib')

class Payload(BaseModel):
    __root__: dict

@app.get('/health')
def health():
    return {'status':'ok'}

@app.post('/predict')
def predict(payload: Payload):
    data = payload.__root__
    df = pd.DataFrame([data])
    try:
        prob = pipeline.predict_proba(df)[:,1][0]
    except Exception as e:
        logger.error(f"Erro na predição: {e}")
        raise HTTPException(status_code=400, detail=str(e))
    return {'score': float(prob)}