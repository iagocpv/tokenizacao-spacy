# Pipeline de Tokenização

Este projeto implementa uma pipeline de tokenização em duas etapas:
1. Tokenização de texto usando spaCy
2. Filtragem de tokens que não são palavras usando expressões regulares

## Requisitos

Para instalar as dependências necessárias:

```
pip install -r requirements.txt
```

Além disso, é necessário baixar o modelo de linguagem do spaCy para português:

```
pip install https://github.com/explosion/spacy-models/releases/download/pt_core_news_sm-3.7.0/pt_core_news_sm-3.7.0.tar.gz
```

## Como usar

Execute o script principal:

```
python tokenizacao.py
```

O script irá:
1. Baixar um texto do Projeto Gutenberg (Dom Casmurro, de Machado de Assis)
2. Tokenizar o texto usando spaCy
3. Filtrar os tokens que não são palavras usando regex
4. Exibir estatísticas sobre o número de tokens antes e depois da filtragem

## Resultados

O script exibirá:
- Número total de tokens após a tokenização com spaCy
- Número total de tokens após a filtragem com regex
- Quantidade e percentual de tokens removidos
- Exemplos dos tokens antes e depois da filtragem