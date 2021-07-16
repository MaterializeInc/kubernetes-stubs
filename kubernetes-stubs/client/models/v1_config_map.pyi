import datetime
import typing

import kubernetes.client

class V1ConfigMap:
    api_version: typing.Optional[str]
    binary_data: typing.Optional[dict[str, str]]
    data: typing.Optional[dict[str, str]]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes.client.V1ObjectMeta]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        binary_data: typing.Optional[dict[str, str]] = ...,
        data: typing.Optional[dict[str, str]] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes.client.V1ObjectMeta] = ...
    ) -> None: ...
