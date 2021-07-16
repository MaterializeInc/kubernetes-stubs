import datetime
import typing

import kubernetes.client

class ExtensionsV1beta1AllowedCSIDriver:
    name: str
    def __init__(self, *, name: str) -> None: ...
