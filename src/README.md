[README.md](https://github.com/user-attachments/files/34244949/README.md)
# src/

Funções do projeto organizadas em módulos reutilizáveis. Elas reproduzem as mesmas
decisões e configurações dos notebooks.

| Arquivo | Responsabilidade |
|---|---|
| `config.py` | caminhos, semente (`RANDOM_STATE = 42`), variável alvo e limiar (nota ≥ 7) |
| `data.py` | carregar o `WineQT.csv` e salvar/ler o `dataset_tratado.csv` |
| `preprocessing.py` | nulos, remoção de `Id` e duplicatas, criação da variável alvo |
| `models.py` | Regressão Logística, Árvore de Decisão e Random Forest, grades do GridSearchCV e treino com `StandardScaler` em `Pipeline` |
| `evaluation.py` | precisão, recall, F1 e AUC da classe Alto e tabela comparativa em `results/metrics/` |

Os notebooks mantêm o código escrito célula a célula, para que a análise possa ser lida
passo a passo junto com as interpretações. Este pacote reúne a mesma lógica para quem
quiser reaproveitá-la fora dos notebooks.

Exemplo, rodando a partir da raiz do repositório:

```python
from sklearn.model_selection import train_test_split

from src.config import RANDOM_STATE, TARGET, TEST_SIZE
from src.data import load_raw
from src.evaluation import comparison_table
from src.models import train_padronizado
from src.preprocessing import preprocess

df = preprocess(load_raw())
X, y = df.drop(TARGET, axis=1), df[TARGET]
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=TEST_SIZE, random_state=RANDOM_STATE, stratify=y
)
grids = train_padronizado(X_train, y_train)
print(comparison_table(grids, X_test, y_test))
```
