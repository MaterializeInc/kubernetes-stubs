import datetime
import typing

import kubernetes.client

class V2beta1MetricStatus:
    container_resource: typing.Optional[
        kubernetes.client.V2beta1ContainerResourceMetricStatus
    ]
    external: typing.Optional[kubernetes.client.V2beta1ExternalMetricStatus]
    object: typing.Optional[kubernetes.client.V2beta1ObjectMetricStatus]
    pods: typing.Optional[kubernetes.client.V2beta1PodsMetricStatus]
    resource: typing.Optional[kubernetes.client.V2beta1ResourceMetricStatus]
    type: str

    def __init__(
        self,
        *,
        container_resource: typing.Optional[
            kubernetes.client.V2beta1ContainerResourceMetricStatus
        ] = ...,
        external: typing.Optional[kubernetes.client.V2beta1ExternalMetricStatus] = ...,
        object: typing.Optional[kubernetes.client.V2beta1ObjectMetricStatus] = ...,
        pods: typing.Optional[kubernetes.client.V2beta1PodsMetricStatus] = ...,
        resource: typing.Optional[kubernetes.client.V2beta1ResourceMetricStatus] = ...,
        type: str
    ) -> None: ...
    def to_dict(self) -> V2beta1MetricStatusDict: ...

class V2beta1MetricStatusDict(typing.TypedDict, total=False):
    containerResource: typing.Optional[
        kubernetes.client.V2beta1ContainerResourceMetricStatusDict
    ]
    external: typing.Optional[kubernetes.client.V2beta1ExternalMetricStatusDict]
    object: typing.Optional[kubernetes.client.V2beta1ObjectMetricStatusDict]
    pods: typing.Optional[kubernetes.client.V2beta1PodsMetricStatusDict]
    resource: typing.Optional[kubernetes.client.V2beta1ResourceMetricStatusDict]
    type: str
