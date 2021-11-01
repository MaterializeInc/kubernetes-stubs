import datetime
import typing

import kubernetes.client

class V1IngressSpec:
    default_backend: typing.Optional[kubernetes.client.V1IngressBackend]
    ingress_class_name: typing.Optional[str]
    rules: typing.Optional[list[kubernetes.client.V1IngressRule]]
    tls: typing.Optional[list[kubernetes.client.V1IngressTLS]]
    def __init__(
        self,
        *,
        default_backend: typing.Optional[kubernetes.client.V1IngressBackend] = ...,
        ingress_class_name: typing.Optional[str] = ...,
        rules: typing.Optional[list[kubernetes.client.V1IngressRule]] = ...,
        tls: typing.Optional[list[kubernetes.client.V1IngressTLS]] = ...
    ) -> None: ...
    def to_dict(self) -> V1IngressSpecDict: ...

class V1IngressSpecDict(typing.TypedDict, total=False):
    defaultBackend: typing.Optional[kubernetes.client.V1IngressBackendDict]
    ingressClassName: typing.Optional[str]
    rules: typing.Optional[list[kubernetes.client.V1IngressRuleDict]]
    tls: typing.Optional[list[kubernetes.client.V1IngressTLSDict]]
