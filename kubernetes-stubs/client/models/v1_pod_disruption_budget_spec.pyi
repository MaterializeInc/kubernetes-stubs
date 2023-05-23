import datetime
import typing

import kubernetes.client

class V1PodDisruptionBudgetSpec:
    max_unavailable: typing.Optional[typing.Any]
    min_available: typing.Optional[typing.Any]
    selector: typing.Optional[kubernetes.client.V1LabelSelector]
    unhealthy_pod_eviction_policy: typing.Optional[str]
    def __init__(
        self,
        *,
        max_unavailable: typing.Optional[typing.Any] = ...,
        min_available: typing.Optional[typing.Any] = ...,
        selector: typing.Optional[kubernetes.client.V1LabelSelector] = ...,
        unhealthy_pod_eviction_policy: typing.Optional[str] = ...
    ) -> None: ...
    def to_dict(self) -> V1PodDisruptionBudgetSpecDict: ...

class V1PodDisruptionBudgetSpecDict(typing.TypedDict, total=False):
    maxUnavailable: typing.Optional[typing.Any]
    minAvailable: typing.Optional[typing.Any]
    selector: typing.Optional[kubernetes.client.V1LabelSelectorDict]
    unhealthyPodEvictionPolicy: typing.Optional[str]
