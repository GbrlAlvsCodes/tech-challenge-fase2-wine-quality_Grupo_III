[README.md](https://github.com/user-attachments/files/34245428/README.md)
## Tech Challenge — Fase 2 | POSTECH Data Analytics

### 1. Identificação

<table>
<tr><th>Campo</th><th>Valor</th></tr>
<tr><td>Turma</td><td>15DTAT</td></tr>
<tr><td>Grupo</td><td>3</td></tr>
<tr><td>Data de entrega</td><td>03/11/2026</td></tr>
</table>

#### Integrantes

<table>
<tr><th>Nome completo</th><th>RM</th><th>E-mail</th></tr>
<tr><td>Gabriel Alves da Silva</td><td>RM376192</td><td>gasmeas10@gmail.com</td></tr>
<tr><td>Dimitria Doi</td><td>RM376922</td><td>dimitria.ro@gmail.com</td></tr>
<tr><td>Breno Plada Delege</td><td>RM377058</td><td>brenoplada@gmail.com</td></tr>
<tr><td>Yan Souza Montes</td><td>RM376051</td><td>yansouzamontes@hotmail.com</td></tr>
</table>

### 2. Links da entrega

<table>
<tr><th>Item</th><th>Link</th></tr>
<tr><td>Repositório</td><td>https://github.com/GbrlAlvsCodes/tech-challenge-fase2-wine-quality_Grupo_III</td></tr>
<tr><td>Vídeo executivo (≤ 5 min)</td><td>https://www.youtube.com/watch?v=o-YT9hCTqB8</td></tr>
<tr><td>Apresentação</td><td>https://github.com/GbrlAlvsCodes/tech-challenge-fase2-wine-quality_Grupo_III/blob/main/docs/apresentacao_executiva.pdf</td></tr>
</table>

### 3. O problema

A avaliação sensorial de vinhos depende de especialistas experientes, o que a torna demorada, cara e sujeita a variações entre avaliadores. Além disso, reunir um painel para analisar grandes volumes de amostras nem sempre é viável. Nesse contexto, o uso de características físico-químicas combinado a técnicas de Machine Learning permite prever a qualidade do vinho de forma rápida e consistente, reduzindo a dependência de avaliações humanas e apoiando decisões mais eficientes de classificação. Assim, este projeto desenvolve modelos de Machine Learning (ML) para classificar vinhos em alta qualidade ou baixa/média qualidade a partir de características físico-químicas.

#### Variável alvo

A variável alvo é a coluna quality (nota de 3 a 8 atribuída por especialistas), convertida em duas categorias:

•	Alta qualidade: nota ≥ 7;

•	Baixa/média qualidade: nota < 7.

A base é desbalanceada: apenas cerca de 13% dos vinhos são de alta qualidade. Por isso, a acurácia isolada pode enganar (um modelo que classificasse todos os vinhos como baixa/média qualidade acertaria cerca de 87% sem de fato distinguir as classes). Assim, a avaliação dos modelos prioriza o F1-score da classe alta, junto com precisão e recall, em vez de considerar apenas a acurácia.

#### Dataset

<table>
<tr><th>Campo</th><th>Valor</th></tr>
<tr><td>Fonte</td><td>https://www.kaggle.com/datasets/yasserh/wine-quality-dataset</td></tr>
<tr><td>Linhas × colunas</td><td>1143 x 13</td></tr>
<tr><td>Período / versão</td><td>1</td></tr>
</table>

Descrição das variáveis principais:

| Variável | Tipo | Descrição |
|-----------|------|------------|
| Acidez fixa (Fixed Acidity) | Número decimal | Quantidade de ácidos não voláteis presentes no vinho. |
| Acidez volátil (Volatile Acidity) | Número decimal | Representa os ácidos voláteis, principalmente o ácido acético. |
| Ácido cítrico (Citric Acid) | Número decimal | Contribui para o frescor e equilíbrio sensorial. |
| Açúcar residual (Residual Sugar) | Número decimal | Quantidade de açúcar que permanece após a fermentação. |
| Cloretos (Chlorides) | Número decimal | Indicador da concentração de sais no vinho. |
| Dióxido de enxofre livre | Número decimal | Proteção contra oxidação e microrganismos. |
| Dióxido de enxofre total | Número decimal | Conservante e estabilizante. |
| Densidade | Número decimal | Relacionada à composição do vinho. |
| pH | Número decimal | Mede a acidez química do vinho. |
| Sulfatos | Número decimal | Auxiliam na preservação e estrutura do vinho. |
| Teor alcoólico | Número decimal | Influencia corpo, aroma e percepção de qualidade. |
| Quality | Número inteiro | Variável-alvo prevista pelo modelo. |
| ID | Número inteiro | Identificador da base. |

### 4. Como reproduzir

```bash
git clone https://github.com/GbrlAlvsCodes/tech-challenge-fase2-wine-quality_Grupo_III.git
cd tech-challenge-fase2-wine-quality_Grupo_III

python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate

pip install -r requirements.txt
jupyter notebook
```
Baixe o dataset e coloque o arquivo bruto em data/raw/ (os dados não são versionados — veja data/README.md).

Depois execute os notebooks nesta ordem:

<table>
<tr><th>#</th><th>Notebook</th><th>O que faz</th></tr>
<tr><td>1</td><td>notebooks/Projeto_II_Vinho.ipynb</td><td>Análise Completa</td></tr>
</table>

**Semente fixa:** RANDOM_STATE = 42

### 5. Resultados

| Modelo | Acurácia | Precisão | Recall | F1 | AUC-ROC |
|---------|----------|----------|--------|----|---------|
| Regressão Logística | 0.79 | 0.36 | 0.78 | 0.49 | 0.88 |
| Árvore de Decisão | 0.81 | 0.40 | 0.78 | 0.52 | 0.79 |
| Random Forest | 0.86 | 0.49 | 0.78 | 0.60 | 0.92 |

**Modelo escolhido:** Random Forest. O modelo apresentou o melhor desempenho geral entre os avaliados, alcançando os melhores resultados nas métricas analisadas.

### 6. Principais conclusões

1. **Álcool:** costuma estar ligado à maturação da uva e a uma fermentação completa, sendo um dos fatores mais influentes na qualidade.
2. **Acidez volátil:** principal fator negativo. O controle de higiene, oxigênio e temperatura ajuda a reduzir seu impacto.
3. **Sulfatos:** níveis adequados contribuem para preservação e qualidade do vinho.

#### Limitações e próximos passos

Uma das principais limitação da base dados é o desbalanceamento da qualidade dos vinhos, que nos trabalhos futuros podem usar o balanceamento para analisar ganho de eficiência. Além disso, recomenda-se confirmar com validação cruzada se todas as variáveis são realmente necessárias no modelo de ML. E o ideal no processo é acompanhar a maturação da uva e a fermentação para monitorar o teor alcoólico, controlar oxigênio, temperatura e higiene do processo para reduzir a acidez volátil e garantir níveis adequados de sulfatos para preservar a qualidade do vinho.

### 7. Estrutura do repositório

├── data/          dados brutos (raw) e tratados (processed) — não versionados

├── notebooks/     análise

└── docs/          apresentação executiva

### 8. Tecnologias

- Python 3.13.18
- pandas 2.2.3
- numpy 2.1.3
- scikit-learn 1.6.1
- matplotlib 3.10.0
- seaborn 0.13.2
- jupyter 1.1.1
