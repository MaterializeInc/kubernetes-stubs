import datetime
import typing

import kubernetes.client

class V2beta2MetricStatus:
    external: typing.Optional[kubernetes.client.V2beta2ExternalMetricStatus]
    object: typing.Optional[kubernetes.client.V2beta2ObjectMetricStatus]
    pods: typing.Optional[kubernetes.client.V2beta2PodsMetricStatus]
    resource: typing.Optional[kubernetes.client.V2beta2ResourceMetricStatus]
    type: str
    def __init__(
        self,
        *,
        external: typing.Optional[kubernetes.client.V2beta2ExternalMetricStatus] = ...,
        object: typing.Optional[kubernetes.client.V2beta2ObjectMetricStatus] = ...,
        pods: typing.Optional[kubernetes.client.V2beta2PodsMetricStatus] = ...,
        resource: typing.Optional[kubernetes.client.V2beta2ResourceMetricStatus] = ...,
        type: str
    ) -> None: ...
