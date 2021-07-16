import datetime
import typing

import kubernetes.client

class V1LimitRangeList:
    api_version: typing.Optional[str]
    items: list[kubernetes.client.V1LimitRange]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes.client.V1ListMeta]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        items: list[kubernetes.client.V1LimitRange],
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes.client.V1ListMeta] = ...
    ) -> None: ...
