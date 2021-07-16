import datetime
import typing

import kubernetes.client

class V1LoadBalancerIngress:
    hostname: typing.Optional[str]
    ip: typing.Optional[str]
    def __init__(
        self, *, hostname: typing.Optional[str] = ..., ip: typing.Optional[str] = ...
    ) -> None: ...
