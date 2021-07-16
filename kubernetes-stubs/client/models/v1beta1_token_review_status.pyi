import datetime
import typing

import kubernetes.client

class V1beta1TokenReviewStatus:
    audiences: typing.Optional[list[str]]
    authenticated: typing.Optional[bool]
    error: typing.Optional[str]
    user: typing.Optional[kubernetes.client.V1beta1UserInfo]
    def __init__(
        self,
        *,
        audiences: typing.Optional[list[str]] = ...,
        authenticated: typing.Optional[bool] = ...,
        error: typing.Optional[str] = ...,
        user: typing.Optional[kubernetes.client.V1beta1UserInfo] = ...
    ) -> None: ...
