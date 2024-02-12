import pandas as pd

from src.mimufs.processing import medico


def test_medico():
    df = pd.DataFrame(
        {
            "Médico Familia": [
                "john doe",
                "jOHN dOE",
                "JOHN DOE",
                "John  Doe",
                "John Doe  ",
                "John Doe      ",
            ]
        }
    )
    # create a dataframe with the same length as df filled with "John Doe" in all cells
    df_expected = pd.DataFrame(
        {"Médico Familia": ["John Doe" for _ in range(df.shape[0])]}
    )

    assert medico(df, column="Médico Familia").equals(df_expected)


"""def test_idade():
    
    df = pd.DataFrame([
        "0 anos",
        "1 ano",
        "56 anos"
    ])
    
    df_expected = pd.DataFrame([
        0,
        1,
        56,
    ])
    
    df_result = idade(df)
    
    print(df_result)
    print(df_expected)
    print(df_result.dtypes)
    print(df_expected.dtypes)
    
    assert df_result.equals(df_expected)"""
