import datetime
import typing

import kubernetes.client

class V2beta1MetricSpec:
    external: typing.Optional[kubernetes.client.V2beta1ExternalMetricSource]
    object: typing.Optional[kubernetes.client.V2beta1ObjectMetricSource]
    pods: typing.Optional[kubernetes.client.V2beta1PodsMetricSource]
    resource: typing.Optional[kubernetes.client.V2beta1ResourceMetricSource]
    type: str
    def __init__(
        self,
        *,
        external: typing.Optional[kubernetes.client.V2beta1ExternalMetricSource] = ...,
        object: typing.Optional[kubernetes.client.V2beta1ObjectMetricSource] = ...,
        pods: typing.Optional[kubernetes.client.V2beta1PodsMetricSource] = ...,
        resource: typing.Optional[kubernetes.client.V2beta1ResourceMetricSource] = ...,
        type: str
    ) -> None: ...
