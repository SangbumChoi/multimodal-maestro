import typer

from maestro.cli.introspection import find_training_recipes
from maestro import __version__

app = typer.Typer()
find_training_recipes(app=app)


@app.command(help="Display information about maestro")
def info():
    typer.echo("Welcome to maestro CLI. Let's train some VLM! 🏋")

@app.command(help="Display version of maestro")
def version():
    typer.echo(f"Maestro version: {__version__}")

if __name__ == "__main__":
    app()
