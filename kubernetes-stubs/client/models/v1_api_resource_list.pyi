import datetime
import typing

import kubernetes.client

class V1APIResourceList:
    api_version: typing.Optional[str]
    group_version: str
    kind: typing.Optional[str]
    resources: list[kubernetes.client.V1APIResource]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        group_version: str,
        kind: typing.Optional[str] = ...,
        resources: list[kubernetes.client.V1APIResource]
    ) -> None: ...
