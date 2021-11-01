import datetime
import typing

import kubernetes.client

class V1Ingress:
    api_version: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes.client.V1ObjectMeta]
    spec: typing.Optional[kubernetes.client.V1IngressSpec]
    status: typing.Optional[kubernetes.client.V1IngressStatus]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes.client.V1ObjectMeta] = ...,
        spec: typing.Optional[kubernetes.client.V1IngressSpec] = ...,
        status: typing.Optional[kubernetes.client.V1IngressStatus] = ...
    ) -> None: ...
    def to_dict(self) -> V1IngressDict: ...

class V1IngressDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes.client.V1ObjectMetaDict]
    spec: typing.Optional[kubernetes.client.V1IngressSpecDict]
    status: typing.Optional[kubernetes.client.V1IngressStatusDict]
