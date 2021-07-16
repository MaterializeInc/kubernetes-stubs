import datetime
import typing

import kubernetes.client

class V1NodeAddress:
    address: str
    type: str
    def __init__(self, *, address: str, type: str) -> None: ...
