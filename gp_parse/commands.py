import asyncio

from typer import Argument, Typer

from .services import get_apps

gp_parser_app = Typer()


@gp_parser_app.command()
def search(query: str = Argument(...)) -> None:
    asyncio.run(get_apps(query))
