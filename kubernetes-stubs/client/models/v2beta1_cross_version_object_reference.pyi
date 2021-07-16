import datetime
import typing

import kubernetes.client

class V2beta1CrossVersionObjectReference:
    api_version: typing.Optional[str]
    kind: str
    name: str
    def __init__(
        self, *, api_version: typing.Optional[str] = ..., kind: str, name: str
    ) -> None: ...
