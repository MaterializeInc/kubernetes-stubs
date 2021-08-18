import datetime
import typing

import kubernetes.client

class ExtensionsV1beta1HTTPIngressPath:
    backend: kubernetes.client.ExtensionsV1beta1IngressBackend
    path: typing.Optional[str]
    path_type: typing.Optional[str]
    def __init__(
        self,
        *,
        backend: kubernetes.client.ExtensionsV1beta1IngressBackend,
        path: typing.Optional[str] = ...,
        path_type: typing.Optional[str] = ...
    ) -> None: ...
