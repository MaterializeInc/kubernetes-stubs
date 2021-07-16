import datetime
import typing

import kubernetes.client

class V1QuobyteVolumeSource:
    group: typing.Optional[str]
    read_only: typing.Optional[bool]
    registry: str
    tenant: typing.Optional[str]
    user: typing.Optional[str]
    volume: str
    def __init__(
        self,
        *,
        group: typing.Optional[str] = ...,
        read_only: typing.Optional[bool] = ...,
        registry: str,
        tenant: typing.Optional[str] = ...,
        user: typing.Optional[str] = ...,
        volume: str
    ) -> None: ...
