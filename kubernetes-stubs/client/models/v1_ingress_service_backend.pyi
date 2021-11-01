import datetime
import typing

import kubernetes.client

class V1IngressServiceBackend:
    name: str
    port: typing.Optional[kubernetes.client.V1ServiceBackendPort]
    def __init__(
        self,
        *,
        name: str,
        port: typing.Optional[kubernetes.client.V1ServiceBackendPort] = ...
    ) -> None: ...
    def to_dict(self) -> V1IngressServiceBackendDict: ...

class V1IngressServiceBackendDict(typing.TypedDict, total=False):
    name: str
    port: typing.Optional[kubernetes.client.V1ServiceBackendPortDict]
