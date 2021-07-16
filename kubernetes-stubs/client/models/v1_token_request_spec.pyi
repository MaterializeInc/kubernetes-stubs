import datetime
import typing

import kubernetes.client

class V1TokenRequestSpec:
    audiences: list[str]
    bound_object_ref: typing.Optional[kubernetes.client.V1BoundObjectReference]
    expiration_seconds: typing.Optional[int]
    def __init__(
        self,
        *,
        audiences: list[str],
        bound_object_ref: typing.Optional[
            kubernetes.client.V1BoundObjectReference
        ] = ...,
        expiration_seconds: typing.Optional[int] = ...
    ) -> None: ...
