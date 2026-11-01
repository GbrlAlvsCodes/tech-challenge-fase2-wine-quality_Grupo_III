# notebooks/

| Arquivo | Escopo |
|---|---|
| `Projeto_II_Vinho.ipynb` | projeto completo em um único notebook: compreensão do problema, análise exploratória (distribuições, outliers, correlações, balanceamento), pré-processamento, modelagem (Regressão Logística, Árvore de Decisão e Random Forest com validação cruzada e GridSearchCV), avaliação (métricas, matriz de confusão, curva ROC), importância das variáveis e implicações práticas |

## Seções do notebook

| Seção | Conteúdo |
|---|---|
| 1. Compreensão do problema | contexto de negócio, fonte e dicionário de variáveis, nulos e duplicatas |
| 2. Análise exploratória | distribuição das notas e das variáveis, outliers, correlações, balanceamento e análise por categoria (Baixo/Médio x Alto) |
| 3. Pré-processamento | decisões sobre nulos, duplicatas, outliers, variável alvo, padronização e feature engineering |
| 4. Modelos | split estratificado, modelos sem ajuste, com GridSearchCV e com GridSearchCV + padronização |
| 5. Comparação dos modelos | métricas da classe Alto, matriz de confusão, curva ROC e escolha do modelo |
| 6. Importância das variáveis | importância no Random Forest, coeficientes da Regressão Logística e aplicações práticas |

## Como executar

1. Baixe o `WineQT.csv` (instruções em `data/README.md`) e salve em `data/raw/WineQT.csv`.
2. O notebook foi desenvolvido no Google Colab e lê o arquivo de `/content/WineQT.csv`:
   - **No Colab:** faça upload do `WineQT.csv` na sessão e rode normalmente.
   - **Localmente:** na segunda célula, troque `CAMINHO_DADOS` para `'../data/raw/WineQT.csv'`.
3. Execute com `Kernel → Restart & Run All`.

