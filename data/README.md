[README.md](https://github.com/user-attachments/files/34244592/README.md)
# data/


| Pasta | Conteúdo |
|---|---|
| `raw/` | `WineQT.csv`, exatamente como baixado do Kaggle, nunca editado |
| `processed/` | `dataset_tratado.csv`, gerado pelo `notebooks/02_preprocessamento.ipynb` |

## Dataset

**Wine Quality Dataset (WineQT)**, disponível no Kaggle. Ele traz análises físico-químicas de vinhos
tintos e a nota de qualidade dada por especialistas.

- 1.143 linhas e 13 colunas (11 variáveis físico-químicas, `quality` e `Id`)
- Sem valores faltantes
- 125 linhas duplicadas, removidas no pré-processamento (1.018 vinhos após a limpeza)
- Dicionário de variáveis: `notebooks/Projeto_II_Vinho.ipynb`, seção 1
