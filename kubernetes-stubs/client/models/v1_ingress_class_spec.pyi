import datetime
import typing

import kubernetes.client

class V1IngressClassSpec:
    controller: typing.Optional[str]
    parameters: typing.Optional[kubernetes.client.V1IngressClassParametersReference]
    def __init__(
        self,
        *,
        controller: typing.Optional[str] = ...,
        parameters: typing.Optional[
            kubernetes.client.V1IngressClassParametersReference
        ] = ...
    ) -> None: ...
    def to_dict(self) -> V1IngressClassSpecDict: ...

class V1IngressClassSpecDict(typing.TypedDict, total=False):
    controller: typing.Optional[str]
    parameters: typing.Optional[kubernetes.client.V1IngressClassParametersReferenceDict]
