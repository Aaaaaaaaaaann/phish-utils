from asyncio import open_connection, gather
from typing import List, Optional
from urllib.parse import urlunparse

from aiohttp import ClientSession
from aiohttp.web import Response
from aiohttp.client_exceptions import ClientError


async def request(url) -> Response:
    async with ClientSession() as session:
        try:
            async with session.get(url) as response:
                return response
        except ClientError:
            return


async def get_server_name(host: str, port: int) -> Optional[str]:
    for scheme in ('https', 'http'):
        url = urlunparse((scheme, f'{host}:{port}', '', '', '', ''))
        if response := await request(url):
            server_name = response.headers.get('server')
            return server_name


async def is_opened(host: str, port: int) -> bool:
    try:
        _, _ = await open_connection(host, port)
    except (ConnectionRefusedError, TimeoutError, OSError):
        return False
    return True


async def check_port(host: str, port: int) -> None:
    if await is_opened(host, port):
        print(f'{host} {port} OPEN')

        if port in (80, 443):
            if server_name := await get_server_name(host, port):
                print(f'{host} {port} SERVER: {server_name}')


async def scan_ports(hosts: List[str], ports: List[int]):
    tasks = [
        check_port(host, port)
        for host in hosts
        for port in ports
    ]
    await gather(*tasks)
