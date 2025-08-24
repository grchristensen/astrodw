import pandas as pd
import pyvo as vo
import typer

app = typer.Typer()
service = vo.dal.TAPService("https://exoplanetarchive.ipac.caltech.edu/TAP")


@app.command()
def main(query: str):
    """
    Queries the NASA exoplanet archive.
    """
    resultset = service.search(query)

    data = resultset.to_table().to_pandas()

    print(data)


if __name__ == "__main__":
    app()

