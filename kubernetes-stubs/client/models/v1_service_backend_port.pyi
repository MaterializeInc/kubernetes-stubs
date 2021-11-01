import datetime
import typing

import kubernetes.client

class V1ServiceBackendPort:
    name: typing.Optional[str]
    number: typing.Optional[int]
    def __init__(
        self, *, name: typing.Optional[str] = ..., number: typing.Optional[int] = ...
    ) -> None: ...
    def to_dict(self) -> V1ServiceBackendPortDict: ...

class V1ServiceBackendPortDict(typing.TypedDict, total=False):
    name: typing.Optional[str]
    number: typing.Optional[int]
