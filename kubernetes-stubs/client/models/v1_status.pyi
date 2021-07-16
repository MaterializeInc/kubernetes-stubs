import datetime
import typing

import kubernetes.client

class V1Status:
    api_version: typing.Optional[str]
    code: typing.Optional[int]
    details: typing.Optional[kubernetes.client.V1StatusDetails]
    kind: typing.Optional[str]
    message: typing.Optional[str]
    metadata: typing.Optional[kubernetes.client.V1ListMeta]
    reason: typing.Optional[str]
    status: typing.Optional[str]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        code: typing.Optional[int] = ...,
        details: typing.Optional[kubernetes.client.V1StatusDetails] = ...,
        kind: typing.Optional[str] = ...,
        message: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes.client.V1ListMeta] = ...,
        reason: typing.Optional[str] = ...,
        status: typing.Optional[str] = ...
    ) -> None: ...
