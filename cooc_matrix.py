"""Taller Presencial Evaluable"""

import pandas as pd


def load_data():
    """Carga datos desde un repo remoto."""
    #
    # Importe el archivo ubicado en
    # https://raw.githubusercontent.com/jdvelasq/datalabs/master/datasets/scopus-papers.csv
    # y retorne un dataframe
    #


def get_keywords(dataframe, colname):
    """Extrae las palabras clave de una columna y las retorna como un pandas.Series"""
    #
    # Cada elemento del pandas.Series es una lista de terminos
    #


def join_keywords(author_keywords, index_keywords):
    """Genera un dataframe concatenando las dos pandas.Series"""


def compute_cooc_table(joined_keywords):
    """Crea una tabla de co-occurrencias."""
    #
    # Cree un dataframe con las columnas 'row', 'col' y 'value'
    #


def compute_cooc_matrix(cooc_table):
    """Crea una matriz de co-occurrencias."""
    #
    # Cree un dataframe donde las filas y columnas son las palabras clave
    # y los valores son la cantidad de veces que co-ocurren


def run():
    """Ejecuta el programa. Salva 'cooc_table.csv' y 'cooc_matrix.csv' en el directorio actual."""


if __name__ == "__main__":
    cooc_matrix = run()
