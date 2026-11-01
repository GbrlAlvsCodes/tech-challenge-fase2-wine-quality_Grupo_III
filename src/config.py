"""Configuração central do projeto: caminhos, semente e constantes.

Os mesmos valores usados nos notebooks (primeira célula de cada um).
"""

from pathlib import Path

# --- Semente -----------------------------------------------------------------
# Usada em todo ponto com aleatoriedade: train_test_split, modelos, CV.
RANDOM_STATE = 42

# --- Caminhos ----------------------------------------------------------------
ROOT = Path(__file__).resolve().parents[1]

DATA_RAW = ROOT / "data" / "raw"
DATA_PROCESSED = ROOT / "data" / "processed"
RESULTS = ROOT / "results"
FIGURES = RESULTS / "figures"
MODELS = RESULTS / "models"
METRICS = RESULTS / "metrics"

# --- Dataset -----------------------------------------------------------------
RAW_FILE = DATA_RAW / "WineQT.csv"
PROCESSED_FILE = DATA_PROCESSED / "dataset_tratado.csv"
TARGET = "qualidade_do_vinho"      # 1 = Alto (nota >= 7), 0 = Baixo/Médio
LIMIAR_ALTO = 7

# --- Split -------------------------------------------------------------------
TEST_SIZE = 0.2
CV_FOLDS = 5
