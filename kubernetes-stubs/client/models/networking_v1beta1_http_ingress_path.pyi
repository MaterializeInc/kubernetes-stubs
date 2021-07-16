import datetime
import typing

import kubernetes.client

class NetworkingV1beta1HTTPIngressPath:
    backend: kubernetes.client.NetworkingV1beta1IngressBackend
    path: typing.Optional[str]
    def __init__(
        self,
        *,
        backend: kubernetes.client.NetworkingV1beta1IngressBackend,
        path: typing.Optional[str] = ...
    ) -> None: ...
