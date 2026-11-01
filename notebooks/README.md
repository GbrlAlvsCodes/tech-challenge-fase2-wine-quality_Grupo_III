[README.md](https://github.com/user-attachments/files/34244471/README.md)
# notebooks/

Ordem numerada obrigatória. Cada notebook roda de cima para baixo em ambiente limpo
(`Kernel → Restart & Run All`) sem erro. É isso que garante a reprodutibilidade.

| Arquivo | Escopo |
|---|---|
| `Projeto_II_Vinho.ipynb` | projeto completo em um único notebook, com todas as etapas e gráficos. Versão original do trabalho, que deu origem aos quatro notebooks acima |

## Como executar

1. Baixe o `WineQT.csv` (instruções em `data/README.md`) e salve em `data/raw/WineQT.csv`.
2. Instale as dependências: `pip install -r requirements.txt`.

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
