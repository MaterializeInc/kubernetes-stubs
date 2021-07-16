import datetime
import typing

import kubernetes.client

class V1TokenReviewSpec:
    audiences: typing.Optional[list[str]]
    token: typing.Optional[str]
    def __init__(
        self,
        *,
        audiences: typing.Optional[list[str]] = ...,
        token: typing.Optional[str] = ...
    ) -> None: ...
