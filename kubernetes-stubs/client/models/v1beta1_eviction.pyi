import datetime
import typing

import kubernetes.client

class V1beta1Eviction:
    api_version: typing.Optional[str]
    delete_options: typing.Optional[kubernetes.client.V1DeleteOptions]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes.client.V1ObjectMeta]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        delete_options: typing.Optional[kubernetes.client.V1DeleteOptions] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes.client.V1ObjectMeta] = ...
    ) -> None: ...
