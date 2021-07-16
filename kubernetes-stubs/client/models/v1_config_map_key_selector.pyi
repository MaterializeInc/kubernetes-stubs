import datetime
import typing

import kubernetes.client

class V1ConfigMapKeySelector:
    key: str
    name: typing.Optional[str]
    optional: typing.Optional[bool]
    def __init__(
        self,
        *,
        key: str,
        name: typing.Optional[str] = ...,
        optional: typing.Optional[bool] = ...
    ) -> None: ...
