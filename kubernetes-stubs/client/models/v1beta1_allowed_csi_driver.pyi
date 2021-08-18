import datetime
import typing

import kubernetes.client

class V1beta1AllowedCSIDriver:
    name: str
    def __init__(self, *, name: str) -> None: ...
