import json
import pytest
from fastapi.testclient import TestClient
from api.main import app

client = TestClient(app)

def test_health():
    r = client.get('/health')
    assert r.status_code == 200
    assert r.json() == {'status':'ok'}


def test_predict_minimal():
    # usa payload com zeros
    payload = {k:0 for k in ['num']}
    r = client.post('/predict', json=payload)
    assert r.status_code == 200
    assert 'score' in r.json()