import datetime
import typing

import kubernetes.client

class V1ResourceQuotaStatus:
    hard: typing.Optional[dict[str, str]]
    used: typing.Optional[dict[str, str]]
    def __init__(
        self,
        *,
        hard: typing.Optional[dict[str, str]] = ...,
        used: typing.Optional[dict[str, str]] = ...
    ) -> None: ...
