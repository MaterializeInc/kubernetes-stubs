import datetime
import typing

import kubernetes.client

class V1ResourceQuotaSpec:
    hard: typing.Optional[dict[str, str]]
    scope_selector: typing.Optional[kubernetes.client.V1ScopeSelector]
    scopes: typing.Optional[list[str]]
    def __init__(
        self,
        *,
        hard: typing.Optional[dict[str, str]] = ...,
        scope_selector: typing.Optional[kubernetes.client.V1ScopeSelector] = ...,
        scopes: typing.Optional[list[str]] = ...
    ) -> None: ...
