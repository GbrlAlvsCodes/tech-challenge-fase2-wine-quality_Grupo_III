"""Definição e treino dos modelos (mesma configuração do notebook 03)."""

from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV, StratifiedKFold
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier

from src.config import CV_FOLDS, RANDOM_STATE


def get_models() -> dict:
    """Os três classificadores. class_weight='balanced' compensa os ~13% de vinhos Alto."""
    return {
        "Regressão Logística": LogisticRegression(random_state=RANDOM_STATE, class_weight="balanced", max_iter=5000),
        "Árvore de Decisão": DecisionTreeClassifier(random_state=RANDOM_STATE, class_weight="balanced"),
        "Random Forest": RandomForestClassifier(random_state=RANDOM_STATE, class_weight="balanced"),
    }


def get_param_grids() -> dict:
    """Combinações testadas no GridSearchCV."""
    return {
        "Regressão Logística": {"C": [0.001, 0.01, 0.1, 1, 10, 100]},
        "Árvore de Decisão": {
            "max_depth": [3, 4, 5, 6, 8, None],
            "min_samples_leaf": [1, 5, 10, 20],
            "criterion": ["gini", "entropy"],
        },
        "Random Forest": {
            "n_estimators": [100, 300],
            "max_depth": [None, 5, 10],
            "min_samples_leaf": [1, 3, 5],
            "criterion": ["gini", "entropy"],
        },
    }


def get_cv() -> StratifiedKFold:
    return StratifiedKFold(n_splits=CV_FOLDS, shuffle=True, random_state=RANDOM_STATE)


def train_padronizado(X_train, y_train) -> dict:
    """GridSearchCV com StandardScaler dentro de um Pipeline (etapa final do notebook 03).

    O scaler é ajustado só no fold de treino de cada divisão, sem vazamento.
    """
    grids = {}
    parametros = get_param_grids()
    for nome, modelo in get_models().items():
        pipeline = Pipeline([("scaler", StandardScaler()), ("modelo", modelo)])
        parametros_pipeline = {"modelo__" + k: v for k, v in parametros[nome].items()}
        grid = GridSearchCV(pipeline, parametros_pipeline, cv=get_cv(), scoring="f1", n_jobs=-1)
        grid.fit(X_train, y_train)
        grids[nome] = grid
    return grids
