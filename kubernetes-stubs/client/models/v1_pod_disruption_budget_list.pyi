import datetime
import typing

import kubernetes.client

class V1PodDisruptionBudgetList:
    api_version: typing.Optional[str]
    items: list[kubernetes.client.V1PodDisruptionBudget]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes.client.V1ListMeta]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        items: list[kubernetes.client.V1PodDisruptionBudget],
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes.client.V1ListMeta] = ...
    ) -> None: ...
    def to_dict(self) -> V1PodDisruptionBudgetListDict: ...

class V1PodDisruptionBudgetListDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    items: list[kubernetes.client.V1PodDisruptionBudgetDict]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes.client.V1ListMetaDict]
