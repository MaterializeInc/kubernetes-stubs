import datetime
import typing

import kubernetes.client

class V2alpha1CronJobList:
    api_version: typing.Optional[str]
    items: list[kubernetes.client.V2alpha1CronJob]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes.client.V1ListMeta]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        items: list[kubernetes.client.V2alpha1CronJob],
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes.client.V1ListMeta] = ...
    ) -> None: ...
