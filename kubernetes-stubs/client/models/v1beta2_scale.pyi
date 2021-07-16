import datetime
import typing

import kubernetes.client

class V1beta2Scale:
    api_version: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes.client.V1ObjectMeta]
    spec: typing.Optional[kubernetes.client.V1beta2ScaleSpec]
    status: typing.Optional[kubernetes.client.V1beta2ScaleStatus]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes.client.V1ObjectMeta] = ...,
        spec: typing.Optional[kubernetes.client.V1beta2ScaleSpec] = ...,
        status: typing.Optional[kubernetes.client.V1beta2ScaleStatus] = ...
    ) -> None: ...
