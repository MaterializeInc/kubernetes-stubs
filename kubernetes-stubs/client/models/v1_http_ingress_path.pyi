import datetime
import typing

import kubernetes.client

class V1HTTPIngressPath:
    backend: kubernetes.client.V1IngressBackend
    path: typing.Optional[str]
    path_type: str
    def __init__(
        self,
        *,
        backend: kubernetes.client.V1IngressBackend,
        path: typing.Optional[str] = ...,
        path_type: str
    ) -> None: ...
    def to_dict(self) -> V1HTTPIngressPathDict: ...

class V1HTTPIngressPathDict(typing.TypedDict, total=False):
    backend: kubernetes.client.V1IngressBackendDict
    path: typing.Optional[str]
    pathType: str
