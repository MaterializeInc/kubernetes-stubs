import datetime
import typing

import kubernetes.client

class V1beta1RuntimeClass:
    api_version: typing.Optional[str]
    handler: str
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes.client.V1ObjectMeta]
    overhead: typing.Optional[kubernetes.client.V1beta1Overhead]
    scheduling: typing.Optional[kubernetes.client.V1beta1Scheduling]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        handler: str,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes.client.V1ObjectMeta] = ...,
        overhead: typing.Optional[kubernetes.client.V1beta1Overhead] = ...,
        scheduling: typing.Optional[kubernetes.client.V1beta1Scheduling] = ...
    ) -> None: ...
