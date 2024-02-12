"""import matplotlib.pyplot as plt
from src.mimufs.visualization import graph_indicador


def test_graph_indicador():
    data = {
        "id_indicador": 1,
        "nome_indicador": "Proporção de consultas realizadas pelo MF",
        "min_aceitavel": 75,
        "max_aceitavel": 92,
        "min_esperado": 78,
        "max_esperado": 90,
        "valor": 80,
    }
    graph = graph_indicador(data)

    assert isinstance(graph, plt.Figure)"""
