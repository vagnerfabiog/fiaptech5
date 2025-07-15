from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer


def build_preprocessor(numeric_features, categorical_features, text_features):
    # Pipeline para numéricos
    numeric_transformer = Pipeline(
        [
            ('imputer', SimpleImputer(strategy='median')),
            ('scaler', StandardScaler()),
        ]
    )

    # Pipeline para categóricos
    categorical_transformer = Pipeline(
        [
            ('imputer', SimpleImputer(strategy='constant', fill_value='missing')),
            ('onehot', OneHotEncoder(handle_unknown='ignore')),
        ]
    )

    # Transformers de texto: TF-IDF para cada campo
    text_transformers = []
    for field in text_features:
        text_transformers.append(
            (f'txt_{field}', TfidfVectorizer(max_features=500), field)
        )

    # Constrói ColumnTransformer
    preprocessor = ColumnTransformer(
        [
            ('num', numeric_transformer, numeric_features),
            ('cat', categorical_transformer, categorical_features),
        ]
        + text_transformers
    )

    return preprocessor
