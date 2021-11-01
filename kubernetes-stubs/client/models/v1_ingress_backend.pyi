import datetime
import typing

import kubernetes.client

class V1IngressBackend:
    resource: typing.Optional[kubernetes.client.V1TypedLocalObjectReference]
    service: typing.Optional[kubernetes.client.V1IngressServiceBackend]
    def __init__(
        self,
        *,
        resource: typing.Optional[kubernetes.client.V1TypedLocalObjectReference] = ...,
        service: typing.Optional[kubernetes.client.V1IngressServiceBackend] = ...
    ) -> None: ...
    def to_dict(self) -> V1IngressBackendDict: ...

class V1IngressBackendDict(typing.TypedDict, total=False):
    resource: typing.Optional[kubernetes.client.V1TypedLocalObjectReferenceDict]
    service: typing.Optional[kubernetes.client.V1IngressServiceBackendDict]
