"""Limpeza e definição da variável alvo (mesmas decisões do notebook 02).

Feature engineering: optamos por manter as 11 variáveis originais.
A justificativa está no notebook 02, seção 4.
"""

import pandas as pd

from src.config import LIMIAR_ALTO, TARGET


def check_missing(df: pd.DataFrame) -> pd.DataFrame:
    """Nulos por coluna, em contagem e percentual."""
    nulos = df.isnull().sum()
    return pd.DataFrame({"nulos": nulos, "%": (nulos / len(df) * 100).round(2)})


def remove_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    """Remove a coluna Id (só numeração da linha) e as linhas duplicadas."""
    return df.drop("Id", axis=1).drop_duplicates()


def qualidade_do_vinho(qualidade: int) -> int:
    """1 = Alto (nota >= 7), 0 = Baixo/Médio (nota < 7)."""
    return 0 if qualidade < LIMIAR_ALTO else 1


def build_target(df: pd.DataFrame) -> pd.DataFrame:
    """Cria a variável alvo binária e remove a nota original (quality)."""
    out = df.copy()
    out[TARGET] = out["quality"].apply(qualidade_do_vinho)
    return out.drop("quality", axis=1)


def preprocess(df_raw: pd.DataFrame) -> pd.DataFrame:
    """Pipeline completo do notebook 02: duplicatas + variável alvo."""
    return build_target(remove_duplicates(df_raw))
