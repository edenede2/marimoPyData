import marimo

__generated_with = "0.17.7"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import numpy as np
    return mo, np


@app.cell
def _(mo):
    s = mo.ui.slider(0,200)
    return (s,)


@app.cell
def _(s):
    s
    return


@app.cell
def _(np, s):
    x = np.arange(0,int(s.value))
    return (x,)


@app.cell
def _(x):
    x
    return


@app.cell
def _():
    return


@app.cell
def _():
    import pandas as pd
    return


@app.cell
def _(s):
    from rich import inspect

    inspect(s)
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
