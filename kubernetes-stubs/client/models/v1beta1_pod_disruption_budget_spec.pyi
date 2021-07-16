import datetime
import typing

import kubernetes.client

class V1beta1PodDisruptionBudgetSpec:
    max_unavailable: typing.Optional[typing.Any]
    min_available: typing.Optional[typing.Any]
    selector: typing.Optional[kubernetes.client.V1LabelSelector]
    def __init__(
        self,
        *,
        max_unavailable: typing.Optional[typing.Any] = ...,
        min_available: typing.Optional[typing.Any] = ...,
        selector: typing.Optional[kubernetes.client.V1LabelSelector] = ...
    ) -> None: ...
