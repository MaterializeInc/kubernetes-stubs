import datetime
import typing

import kubernetes.client

class V1EndpointPort:
    name: typing.Optional[str]
    port: int
    protocol: typing.Optional[str]
    def __init__(
        self,
        *,
        name: typing.Optional[str] = ...,
        port: int,
        protocol: typing.Optional[str] = ...
    ) -> None: ...
