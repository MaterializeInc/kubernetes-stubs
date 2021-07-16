import datetime
import typing

import kubernetes.client

class ExtensionsV1beta1IngressSpec:
    backend: typing.Optional[kubernetes.client.ExtensionsV1beta1IngressBackend]
    rules: typing.Optional[list[kubernetes.client.ExtensionsV1beta1IngressRule]]
    tls: typing.Optional[list[kubernetes.client.ExtensionsV1beta1IngressTLS]]
    def __init__(
        self,
        *,
        backend: typing.Optional[
            kubernetes.client.ExtensionsV1beta1IngressBackend
        ] = ...,
        rules: typing.Optional[
            list[kubernetes.client.ExtensionsV1beta1IngressRule]
        ] = ...,
        tls: typing.Optional[list[kubernetes.client.ExtensionsV1beta1IngressTLS]] = ...
    ) -> None: ...
