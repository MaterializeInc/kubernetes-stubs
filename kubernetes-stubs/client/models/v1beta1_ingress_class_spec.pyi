import datetime
import typing

import kubernetes.client

class V1beta1IngressClassSpec:
    controller: typing.Optional[str]
    parameters: typing.Optional[
        kubernetes.client.V1beta1IngressClassParametersReference
    ]
    def __init__(
        self,
        *,
        controller: typing.Optional[str] = ...,
        parameters: typing.Optional[
            kubernetes.client.V1beta1IngressClassParametersReference
        ] = ...
    ) -> None: ...
    def to_dict(self) -> V1beta1IngressClassSpecDict: ...

class V1beta1IngressClassSpecDict(typing.TypedDict, total=False):
    controller: typing.Optional[str]
    parameters: typing.Optional[
        kubernetes.client.V1beta1IngressClassParametersReferenceDict
    ]
