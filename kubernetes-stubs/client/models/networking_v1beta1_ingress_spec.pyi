import datetime
import typing

import kubernetes.client

class NetworkingV1beta1IngressSpec:
    backend: typing.Optional[kubernetes.client.NetworkingV1beta1IngressBackend]
    rules: typing.Optional[list[kubernetes.client.NetworkingV1beta1IngressRule]]
    tls: typing.Optional[list[kubernetes.client.NetworkingV1beta1IngressTLS]]
    def __init__(
        self,
        *,
        backend: typing.Optional[
            kubernetes.client.NetworkingV1beta1IngressBackend
        ] = ...,
        rules: typing.Optional[
            list[kubernetes.client.NetworkingV1beta1IngressRule]
        ] = ...,
        tls: typing.Optional[list[kubernetes.client.NetworkingV1beta1IngressTLS]] = ...
    ) -> None: ...
