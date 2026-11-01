"""Métricas e comparação entre modelos (mesmas métricas do notebook 04)."""

import pandas as pd
from sklearn.metrics import (
    accuracy_score,
    f1_score,
    precision_score,
    recall_score,
    roc_auc_score,
)

from src.config import METRICS


def score(y_true, y_pred, y_proba=None) -> dict:
    """Métricas da classe Alto. Acurácia sozinha engana: prever sempre Baixo/Médio já dá ~87%."""
    out = {
        "Taxa de acerto": accuracy_score(y_true, y_pred),
        "Precisão": precision_score(y_true, y_pred),
        "Recall": recall_score(y_true, y_pred),
        "F1": f1_score(y_true, y_pred),
    }
    if y_proba is not None:
        out["AUC"] = roc_auc_score(y_true, y_proba)
    return out


def comparison_table(grids: dict, X_test, y_test, nome_arquivo: str = "comparacao_modelos.csv") -> pd.DataFrame:
    """Avalia os modelos no teste, monta a tabela e salva em results/metrics/."""
    linhas = {}
    for nome, grid in grids.items():
        modelo = grid.best_estimator_
        linhas[nome] = score(y_test, modelo.predict(X_test), modelo.predict_proba(X_test)[:, 1])
        linhas[nome]["F1 (validação cruzada)"] = grid.best_score_
    df = pd.DataFrame(linhas).T.round(2).sort_values("F1", ascending=False)
    METRICS.mkdir(parents=True, exist_ok=True)
    df.to_csv(METRICS / nome_arquivo)
    return df
