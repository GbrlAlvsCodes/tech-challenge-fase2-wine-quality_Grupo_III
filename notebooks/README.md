[README.md](https://github.com/user-attachments/files/34244471/README.md)
# notebooks/

Ordem numerada obrigatória. Cada notebook roda de cima para baixo em ambiente limpo
(`Kernel → Restart & Run All`) sem erro. É isso que garante a reprodutibilidade.

| Arquivo | Escopo |
|---|---|
| `01_eda.ipynb` | visão geral e dicionário de variáveis, distribuições, outliers, correlações, balanceamento, análise por categoria (Baixo/Médio x Alto) e síntese da EDA |
| `02_preprocessamento.ipynb` | nulos, duplicatas, definição do alvo (nota ≥ 7 = Alto), padronização e feature engineering; gera `data/processed/dataset_tratado.csv` |
| `03_modelagem.ipynb` | split treino/teste estratificado, validação cruzada (5 folds), Regressão Logística, Árvore de Decisão e Random Forest em três etapas (sem ajuste, GridSearchCV, GridSearchCV + padronização); salva os modelos em `results/models/` |
| `04_avaliacao.ipynb` | métricas no teste (precisão, recall, F1, AUC-ROC), matriz de confusão, curva ROC, importância das variáveis, implicações práticas e limitações |
| `Projeto_II_Vinho.ipynb` | projeto completo em um único notebook, com todas as etapas e gráficos. Versão original do trabalho, que deu origem aos quatro notebooks acima |

## Como executar

1. Baixe o `WineQT.csv` (instruções em `data/README.md`) e salve em `data/raw/WineQT.csv`.
2. Instale as dependências: `pip install -r requirements.txt`.
3. Abra os notebooks a partir desta pasta (`notebooks/`) e rode na ordem **01 → 02 → 03 → 04**.
   Cada um depende do arquivo gerado pelo anterior:

```
data/raw/WineQT.csv
      │
      ▼
01_eda ──► 02_preprocessamento ──► data/processed/dataset_tratado.csv
                                            │
                                            ▼
                                     03_modelagem ──► results/models/grids_padronizados.joblib
                                                                │
                                                                ▼
                                                         04_avaliacao
```

`Projeto_II_Vinho.ipynb` não depende dos outros: lê o CSV direto e roda tudo sozinho.
Ele foi desenvolvido no Google Colab, então o caminho do arquivo aponta para
`/content/WineQT.csv`. Para rodar localmente, troque `CAMINHO_DADOS` para
`'../data/raw/WineQT.csv'`.

## Regras

- **Antes do commit:** verifique que a numeração das células está em ordem crescente
  (`[1]`, `[2]`, `[3]`...). Células fora de ordem indicam execução caótica.
- Mantenha as saídas dos gráficos salvas no notebook. O avaliador precisa ver os
  resultados sem executar nada.
- Todo gráfico tem um parágrafo de interpretação em markdown logo abaixo.
- A primeira célula de cada notebook define `RANDOM_STATE = 42` e os caminhos.
  O valor é o mesmo em todos os notebooks.
