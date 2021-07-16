import datetime
import typing

import kubernetes.client

class V1Endpoints:
    api_version: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes.client.V1ObjectMeta]
    subsets: typing.Optional[list[kubernetes.client.V1EndpointSubset]]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes.client.V1ObjectMeta] = ...,
        subsets: typing.Optional[list[kubernetes.client.V1EndpointSubset]] = ...
    ) -> None: ...
