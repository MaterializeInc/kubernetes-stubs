import datetime
import typing

import kubernetes.client

class V1CSINodeSpec:
    drivers: list[kubernetes.client.V1CSINodeDriver]
    def __init__(self, *, drivers: list[kubernetes.client.V1CSINodeDriver]) -> None: ...
