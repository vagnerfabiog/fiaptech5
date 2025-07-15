import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn.model_selection import cross_val_score
from .data_loader import load_data
from features import build_preprocessor


def main():
    # 1) Carrega dados
    df = load_data()
    X = df.drop(columns=['job_id', 'applicant_id', 'status', 'target'])
    y = df['target']

    # 2) Define listas de colunas
    numeric_features = [
        col for col in X.select_dtypes(include=['int64', 'float64']).columns
    ]
    categorical_features = [
        col for col in X.select_dtypes(include=['object']).columns
        if col not in ['descricao_vaga', 'requisitos', 'resumo_candidato']
    ]
    text_features = [
        'descricao_vaga',
        'requisitos',
        'resumo_candidato',
        'titulo',
    ]

    # 3) Pipeline
    preprocessor = build_preprocessor(
        numeric_features, categorical_features, text_features
    )
    pipeline = Pipeline(
        [
            ('preproc', preprocessor),
            ('clf', RandomForestClassifier(n_estimators=100, random_state=42)),
        ]
    )

    # 4) Avaliar com cross-validation
    scores = cross_val_score(
        pipeline,
        X,
        y,
        cv=5,
        scoring='roc_auc',
    )
    print(f'Mean ROC-AUC: {scores.mean():.4f}')

    # 5) Treinar no dataset completo e salvar modelo
    pipeline.fit(X, y)
    joblib.dump(pipeline, 'model.joblib')
    print('Modelo salvo em model.joblib')


if __name__ == '__main__':
    main()
