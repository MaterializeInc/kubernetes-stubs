import datetime
import typing

import kubernetes.client

class V1StatusCause:
    field: typing.Optional[str]
    message: typing.Optional[str]
    reason: typing.Optional[str]
    def __init__(
        self,
        *,
        field: typing.Optional[str] = ...,
        message: typing.Optional[str] = ...,
        reason: typing.Optional[str] = ...
    ) -> None: ...
