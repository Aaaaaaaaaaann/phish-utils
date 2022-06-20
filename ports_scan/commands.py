from typing import List
import asyncio

from typer import Argument, Typer

from .utils import split_hosts
from .services import scan_ports

ports_scan_app = Typer()


@ports_scan_app.command()
def scan(hosts: str = Argument(...), ports: List[int] = Argument(...)) -> None:
    hosts = split_hosts(hosts)
    asyncio.run(scan_ports(hosts, ports))
