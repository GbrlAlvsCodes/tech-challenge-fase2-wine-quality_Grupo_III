"""Carregamento e persistência de dados."""

import pandas as pd

from src.config import PROCESSED_FILE, RAW_FILE


def load_raw() -> pd.DataFrame:
    """Lê o WineQT.csv de data/raw/ sem nenhuma transformação."""
    if not RAW_FILE.exists():
        raise FileNotFoundError(
            f"{RAW_FILE} não encontrado. Veja data/README.md para baixar o dataset."
        )
    return pd.read_csv(RAW_FILE)


def save_processed(df: pd.DataFrame) -> None:
    """Grava o dataset tratado em data/processed/dataset_tratado.csv."""
    PROCESSED_FILE.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(PROCESSED_FILE, index=False)


def load_processed() -> pd.DataFrame:
    """Lê o dataset tratado gerado pelo notebook 02."""
    return pd.read_csv(PROCESSED_FILE)
