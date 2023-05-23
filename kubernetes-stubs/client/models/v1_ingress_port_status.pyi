import datetime
import typing

import kubernetes.client

class V1IngressPortStatus:
    error: typing.Optional[str]
    port: int
    protocol: str
    def __init__(
        self, *, error: typing.Optional[str] = ..., port: int, protocol: str
    ) -> None: ...
    def to_dict(self) -> V1IngressPortStatusDict: ...

class V1IngressPortStatusDict(typing.TypedDict, total=False):
    error: typing.Optional[str]
    port: int
    protocol: str
