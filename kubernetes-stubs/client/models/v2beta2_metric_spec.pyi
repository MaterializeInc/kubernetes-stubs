import datetime
import typing

import kubernetes.client

class V2beta2MetricSpec:
    external: typing.Optional[kubernetes.client.V2beta2ExternalMetricSource]
    object: typing.Optional[kubernetes.client.V2beta2ObjectMetricSource]
    pods: typing.Optional[kubernetes.client.V2beta2PodsMetricSource]
    resource: typing.Optional[kubernetes.client.V2beta2ResourceMetricSource]
    type: str
    def __init__(
        self,
        *,
        external: typing.Optional[kubernetes.client.V2beta2ExternalMetricSource] = ...,
        object: typing.Optional[kubernetes.client.V2beta2ObjectMetricSource] = ...,
        pods: typing.Optional[kubernetes.client.V2beta2PodsMetricSource] = ...,
        resource: typing.Optional[kubernetes.client.V2beta2ResourceMetricSource] = ...,
        type: str
    ) -> None: ...
