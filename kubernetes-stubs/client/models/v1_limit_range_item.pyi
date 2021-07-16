import datetime
import typing

import kubernetes.client

class V1LimitRangeItem:
    default: typing.Optional[dict[str, str]]
    default_request: typing.Optional[dict[str, str]]
    max: typing.Optional[dict[str, str]]
    max_limit_request_ratio: typing.Optional[dict[str, str]]
    min: typing.Optional[dict[str, str]]
    type: typing.Optional[str]
    def __init__(
        self,
        *,
        default: typing.Optional[dict[str, str]] = ...,
        default_request: typing.Optional[dict[str, str]] = ...,
        max: typing.Optional[dict[str, str]] = ...,
        max_limit_request_ratio: typing.Optional[dict[str, str]] = ...,
        min: typing.Optional[dict[str, str]] = ...,
        type: typing.Optional[str] = ...
    ) -> None: ...
