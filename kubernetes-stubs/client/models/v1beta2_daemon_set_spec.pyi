import datetime
import typing

import kubernetes.client

class V1beta2DaemonSetSpec:
    min_ready_seconds: typing.Optional[int]
    revision_history_limit: typing.Optional[int]
    selector: kubernetes.client.V1LabelSelector
    template: kubernetes.client.V1PodTemplateSpec
    update_strategy: typing.Optional[kubernetes.client.V1beta2DaemonSetUpdateStrategy]
    def __init__(
        self,
        *,
        min_ready_seconds: typing.Optional[int] = ...,
        revision_history_limit: typing.Optional[int] = ...,
        selector: kubernetes.client.V1LabelSelector,
        template: kubernetes.client.V1PodTemplateSpec,
        update_strategy: typing.Optional[
            kubernetes.client.V1beta2DaemonSetUpdateStrategy
        ] = ...
    ) -> None: ...
