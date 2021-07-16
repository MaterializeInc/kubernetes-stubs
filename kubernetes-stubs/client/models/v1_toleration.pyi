import datetime
import typing

import kubernetes.client

class V1Toleration:
    effect: typing.Optional[str]
    key: typing.Optional[str]
    operator: typing.Optional[str]
    toleration_seconds: typing.Optional[int]
    value: typing.Optional[str]
    def __init__(
        self,
        *,
        effect: typing.Optional[str] = ...,
        key: typing.Optional[str] = ...,
        operator: typing.Optional[str] = ...,
        toleration_seconds: typing.Optional[int] = ...,
        value: typing.Optional[str] = ...
    ) -> None: ...
