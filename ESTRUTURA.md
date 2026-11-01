## Estrutura do repositório

```

├── CHECKLIST.md
├── ESTRUTURA.md
├── LICENSE
├── README.md                          este arquivo
├── requirements.txt                   bibliotecas usadas, com versões fixas
│
├── data/
│   ├── README.md                      instruções para baixar o dataset
│   ├── raw/                           vazio no Git — WineQT.csv baixado do Kaggle
│   └── processed/                     vazio no Git — não utilizado (o notebook trata os dados em memória)
│
├── docs/
│   ├── README.md
│   └── apresentacao_executiva.pdf     apresentação executiva
│
├── notebooks/
│   ├── README.md                      seções do notebook e como executar
│   └── Projeto_II_Vinho.ipynb         projeto completo: EDA, pré-processamento, modelagem e avaliação
│
├── results/
│   ├── README.md
│   ├── figures/                       14 gráficos do projeto exportados em .png
│   ├── metrics/                       comparacao_etapas.csv e modelos_finais_teste.csv
│   └── models/                        vazio no Git — modelos são regenerados rodando o notebook
│
├── src/
│   ├── README.md
│   ├── config.py                      caminhos, semente e variável alvo
│   ├── data.py                        leitura e gravação dos dados
│   ├── preprocessing.py               duplicatas e criação da variável alvo
│   ├── models.py                      modelos e grades do GridSearchCV
│   └── evaluation.py                  métricas da classe Alto
│
└── submissao/
    ├── README.md
    ├── entrega.json                   identificação do grupo e links da entrega
    └── gerar_submissao.py             gera o PDF de submissão
```
