import datetime
import typing

import kubernetes.client

class V1ComponentCondition:
    error: typing.Optional[str]
    message: typing.Optional[str]
    status: str
    type: str
    def __init__(
        self,
        *,
        error: typing.Optional[str] = ...,
        message: typing.Optional[str] = ...,
        status: str,
        type: str
    ) -> None: ...
