from typer import Argument, Typer

from .services import get_matches

domains_match_app = Typer()


@domains_match_app.command()
def match(keyword: str = Argument(...)) -> None:
    get_matches(keyword)
