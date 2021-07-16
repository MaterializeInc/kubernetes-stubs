import datetime
import typing

import kubernetes.client

class V1NamespaceStatus:
    conditions: typing.Optional[list[kubernetes.client.V1NamespaceCondition]]
    phase: typing.Optional[str]
    def __init__(
        self,
        *,
        conditions: typing.Optional[list[kubernetes.client.V1NamespaceCondition]] = ...,
        phase: typing.Optional[str] = ...
    ) -> None: ...
