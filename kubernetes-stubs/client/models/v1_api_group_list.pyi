import datetime
import typing

import kubernetes.client

class V1APIGroupList:
    api_version: typing.Optional[str]
    groups: list[kubernetes.client.V1APIGroup]
    kind: typing.Optional[str]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        groups: list[kubernetes.client.V1APIGroup],
        kind: typing.Optional[str] = ...
    ) -> None: ...
