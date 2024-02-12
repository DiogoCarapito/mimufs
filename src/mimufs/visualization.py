"""
Visualization module for the MIMUFS package
"""

"""import pandas as pd
import matplotlib.pyplot as plt


def graph_indicador(*args, **kwargs):
    # Variable names that will be extracted from the DataFrame or kwargs
    variables = [
        "id_indicador",
        "nome_indicador",
        "min_aceitavel",
        "min_esperado",
        "max_esperado",
        "max_aceitavel",
        "valor",
    ]

    # check if the first argument is a DataFrame
    if len(args) > 0 and isinstance(args[0], pd.DataFrame):
        df = args[0]
        try:
            # Extract variables from DataFrame
            for var in variables:
                globals()[var] = df[var]
        except KeyError:
            raise ValueError(f"DataFrame must contain the following column: {var}")

    # check if the first argument is a dictionary
    elif len(args) > 0 and isinstance(args[0], dict):
        data = args[0]
        for var in variables:
            if var not in data:
                raise ValueError(f"Value for {var} was not provided")
            else:
                globals()[var] = data.get(var)

    # check if the variables are provided as kwargs
    else:
        for var in variables:
            if var not in kwargs:
                raise ValueError(f"Value for {var} was not provided")
            else:
                globals()[var] = kwargs.get(var)

    # Define the colors
    colors = ["red", "yellow", "green", "yellow", "red"]

    # Define the ranges of the colors
    ranges = [
        (0, min_aceitavel),
        (min_aceitavel, min_esperado),
        (min_esperado, max_esperado),
        (max_esperado, max_aceitavel),
        (max_aceitavel, 100),
    ]

    # Create the figure and axis
    fig, ax = plt.subplots(figsize=(5, 0.75))

    # Add the background areas
    for color, (start, end) in zip(colors, ranges):
        ax.axvspan(start, end, facecolor=color, alpha=0.3)

    # Plot the indicator value
    bar = ax.barh(
        id_indicador, valor, height=0.6, color=(46 / 255, 80 / 255, 140 / 255, 1)
    )

    # Convert the indicator ID to float for ylimit and yticks
    id_float = float(id_indicador)

    # Set the plot limits and ticks
    ax.set_xlim(0, 100)
    ax.set_ylim(id_float - 0.5, id_float + 0.5)
    ax.set_yticks([])
    ax.set_xticks([min_aceitavel, min_esperado, max_esperado, max_aceitavel])

    # Set the y-label and title
    ax.set_title(f"{id_indicador} - {nome_indicador}")

    # Add the value label
    rect = bar[0]
    width = rect.get_width()
    ax.text(
        width, rect.get_y() + rect.get_height() / 2, f"{width}%", ha="left", va="center"
    )

    return fig
"""
