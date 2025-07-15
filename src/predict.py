import joblib
import pandas as pd
import argparse


def main(input_json):
    pipeline = joblib.load('model.joblib')
    df = pd.read_json(input_json, orient='index').T  # assume dict único
    score = pipeline.predict_proba(df)[:,1][0]
    print(f'Probabilidade de contratação: {score:.4f}')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', required=True, help='Caminho para JSON de input')
    args = parser.parse_args()
    main(args.input)