import pandas as pd
from sklearn.pipeline import Pipeline
from src.features import build_preprocessor

def test_preprocessor_shapes():
    X = pd.DataFrame({
        'num':[1,2,3],
        'cat':['a','b','a'],
        'texto':['ola','mundo','teste']
    })
    pre = build_preprocessor(['num'], ['cat'], ['texto'])
    Xt = pre.fit_transform(X)
    # deve retornar matriz 3x?
    assert Xt.shape[0] == 3