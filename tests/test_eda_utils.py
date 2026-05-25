import pandas as pd
from src import eda_utils


def test_column_exists():
    df = pd.DataFrame({"A": [1, 2, 3]})

    assert "A" in df.columns


def test_plot_histogram_does_not_crash():
    df = pd.DataFrame({"A": [1, 2, 3, 4, 5]})

    # should not raise error
    eda_utils.plot_histogram(df, "A")


def test_plot_scatter_does_not_crash():
    df = pd.DataFrame({
        "A": [1, 2, 3],
        "B": [4, 5, 6]
    })

    eda_utils.plot_scatter(df, "A", "B")