"""_summary_
This module contains the functions to process the data from BI-CSP and MIM@UF datasets.
"""

import pandas as pd

# import re


def medico(df: pd.DataFrame, column="Médico Familia") -> pd.DataFrame:
    
    # convert the string to title case
    df[column] = df[column].str.title()

    # remove the double spaces in the string
    df[column] = df[column].str.replace("  ", " ")

    # remove the last space in the string
    df[column] = df[column].str.rstrip()

    return df


"""def idade(df: pd.DataFrame) -> pd.DataFrame:
    
    # remover os caracteres não numéricos
    df[column] = df[column].apply(lambda x: re.sub(r'\D+', '', x))
    

    # converter para inteiro
    df[column] = pd.to_numeric(df[column])
    
    # converter para int64
    df[column] = df[column].astype('int64')
    
    return df[column]"""
