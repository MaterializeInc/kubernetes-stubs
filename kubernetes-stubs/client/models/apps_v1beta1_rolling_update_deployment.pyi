import datetime
import typing

import kubernetes.client

class AppsV1beta1RollingUpdateDeployment:
    max_surge: typing.Optional[typing.Any]
    max_unavailable: typing.Optional[typing.Any]
    def __init__(
        self,
        *,
        max_surge: typing.Optional[typing.Any] = ...,
        max_unavailable: typing.Optional[typing.Any] = ...
    ) -> None: ...
