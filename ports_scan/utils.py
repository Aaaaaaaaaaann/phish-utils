from typing import List


def split_hosts(hosts: str) -> List[str]:
    if hosts.rfind('/') < 0:
        return hosts

    network_id, _, hosts_ids = hosts.rpartition('.')
    start_host, _, end_host = hosts_ids.partition('/')
    ips = [
        f'{network_id}.{host_id}'
        for host_id
        in range(int(start_host), int(end_host) + 1)
    ]
    return ips
