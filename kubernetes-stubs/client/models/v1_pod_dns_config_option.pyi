import datetime
import typing

import kubernetes.client

class V1PodDNSConfigOption:
    name: typing.Optional[str]
    value: typing.Optional[str]
    def __init__(
        self, *, name: typing.Optional[str] = ..., value: typing.Optional[str] = ...
    ) -> None: ...
