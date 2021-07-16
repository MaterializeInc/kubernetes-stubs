import datetime
import typing

import kubernetes.client

class ExtensionsV1beta1Scale:
    api_version: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes.client.V1ObjectMeta]
    spec: typing.Optional[kubernetes.client.ExtensionsV1beta1ScaleSpec]
    status: typing.Optional[kubernetes.client.ExtensionsV1beta1ScaleStatus]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes.client.V1ObjectMeta] = ...,
        spec: typing.Optional[kubernetes.client.ExtensionsV1beta1ScaleSpec] = ...,
        status: typing.Optional[kubernetes.client.ExtensionsV1beta1ScaleStatus] = ...
    ) -> None: ...
