import datetime
import typing

import kubernetes.client

class CoreV1EndpointPort:
    app_protocol: typing.Optional[str]
    name: typing.Optional[str]
    port: int
    protocol: typing.Optional[str]

    def __init__(
        self,
        *,
        app_protocol: typing.Optional[str] = ...,
        name: typing.Optional[str] = ...,
        port: int,
        protocol: typing.Optional[str] = ...
    ) -> None: ...
    def to_dict(self) -> CoreV1EndpointPortDict: ...

class CoreV1EndpointPortDict(typing.TypedDict, total=False):
    appProtocol: typing.Optional[str]
    name: typing.Optional[str]
    port: int
    protocol: typing.Optional[str]
