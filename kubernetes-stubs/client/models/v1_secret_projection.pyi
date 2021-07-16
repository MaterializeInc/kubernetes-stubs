import datetime
import typing

import kubernetes.client

class V1SecretProjection:
    items: typing.Optional[list[kubernetes.client.V1KeyToPath]]
    name: typing.Optional[str]
    optional: typing.Optional[bool]
    def __init__(
        self,
        *,
        items: typing.Optional[list[kubernetes.client.V1KeyToPath]] = ...,
        name: typing.Optional[str] = ...,
        optional: typing.Optional[bool] = ...
    ) -> None: ...
