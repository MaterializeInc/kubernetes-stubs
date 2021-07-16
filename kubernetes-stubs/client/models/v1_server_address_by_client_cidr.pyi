import datetime
import typing

import kubernetes.client

class V1ServerAddressByClientCIDR:
    client_cidr: str
    server_address: str
    def __init__(self, *, client_cidr: str, server_address: str) -> None: ...
