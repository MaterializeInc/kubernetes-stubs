import datetime
import typing

import kubernetes.client

class PolicyV1beta1HostPortRange:
    max: int
    min: int
    def __init__(self, *, max: int, min: int) -> None: ...
