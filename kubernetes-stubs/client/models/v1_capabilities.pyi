import datetime
import typing

import kubernetes.client

class V1Capabilities:
    add: typing.Optional[list[str]]
    drop: typing.Optional[list[str]]
    def __init__(
        self,
        *,
        add: typing.Optional[list[str]] = ...,
        drop: typing.Optional[list[str]] = ...
    ) -> None: ...
