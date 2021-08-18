import datetime
import typing

import kubernetes.client

class V1beta1IngressClassSpec:
    controller: typing.Optional[str]
    parameters: typing.Optional[kubernetes.client.V1TypedLocalObjectReference]
    def __init__(
        self,
        *,
        controller: typing.Optional[str] = ...,
        parameters: typing.Optional[kubernetes.client.V1TypedLocalObjectReference] = ...
    ) -> None: ...