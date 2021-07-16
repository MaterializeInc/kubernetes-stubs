import datetime
import typing

import kubernetes.client

class NetworkingV1beta1Ingress:
    api_version: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes.client.V1ObjectMeta]
    spec: typing.Optional[kubernetes.client.NetworkingV1beta1IngressSpec]
    status: typing.Optional[kubernetes.client.NetworkingV1beta1IngressStatus]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes.client.V1ObjectMeta] = ...,
        spec: typing.Optional[kubernetes.client.NetworkingV1beta1IngressSpec] = ...,
        status: typing.Optional[kubernetes.client.NetworkingV1beta1IngressStatus] = ...
    ) -> None: ...
