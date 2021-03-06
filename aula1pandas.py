# -*- coding: utf-8 -*-
"""Aula1Pandas.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ujcvtva06mWtFtBe_sg749gpUu8J4Pep
"""

#importando a biblioteca pandas 
import pandas as pd

#fazendo a leitura do arquivo 
df = pd.read_csv("/content/Gapminder.csv", error_bad_lines=False, sep=';')

#visualizando as 5 primeiras linhas
df.head()

#alterando o titulo das colunas
df = df.rename(columns={'country':'Pais', 'continent':'Continente', 'year':'Ano', 'lifeExp':'Expectativa de Vida', 'pop':'Pop','gdpPercap':'PIB'})

#total de linhas e colunas
df.shape

#consulta tds as colunas
df.columns

#tipo de dado q tem em cada coluna
df.dtypes

#mostra as ultimas linhas do dataframe
df.tail()

#retorna informações estatistica dos arquivos
df.describe()

#mostra os dados da coluna
df['Continente'].unique()

#mostrando os valores apenas de um dado especifico com filtro loc
Oceania = df.loc[df['Continente'] == 'Oceania']
Oceania.head()

Oceania['Continente'].unique()

#fazendo uma contagem cada dado da coluna
df.groupby('Continente')['Pais'].nunique()

#traz a media dos dados 
df.groupby('Ano')['Expectativa de Vida'].mean()