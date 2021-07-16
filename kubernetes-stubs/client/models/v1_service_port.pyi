import datetime
import typing

import kubernetes.client

class V1ServicePort:
    name: typing.Optional[str]
    node_port: typing.Optional[int]
    port: int
    protocol: typing.Optional[str]
    target_port: typing.Optional[typing.Any]
    def __init__(
        self,
        *,
        name: typing.Optional[str] = ...,
        node_port: typing.Optional[int] = ...,
        port: int,
        protocol: typing.Optional[str] = ...,
        target_port: typing.Optional[typing.Any] = ...
    ) -> None: ...
