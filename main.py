from typer import Typer

from ports_scan.commands import ports_scan_app
from domains_match.commands import domains_match_app
from gp_parse.commands import gp_parser_app


def main() -> None:
    app = Typer()

    app.add_typer(ports_scan_app, name='ports')
    app.add_typer(domains_match_app, name='domains')
    app.add_typer(gp_parser_app, name='gp')

    app()


if __name__ == '__main__':
    main()
