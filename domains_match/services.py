from typing import Dict, List

import dnstwist

from .utils import domains_list


def print_result(data: List[Dict]) -> None:
    for row in data:
        domain = row['domain']
        dns_a = row.get('dns_a', [])
        dns_aaaa = row.get('dns_aaaa', [])

        ips = [
            value for value
            in [*dns_a, *dns_aaaa]
            if not value.startswith('!')
        ]
        if not ips:
            continue

        ips = ', '.join(ips)
        print(f'{domain:25} {ips}')


def get_data(domain: str) -> List[Dict]:
    data = dnstwist.run(
        domain=domain,
        registered=True,
        format='null',
        threads=50,
    )
    return data


def get_matches(keyword: str) -> None:
    for domain in domains_list:
        data = get_data(domain=f'{keyword}.{domain}')
        print_result(data)
