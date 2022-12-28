import datetime
import typing

import kubernetes.client

class V2beta2MetricStatus:
    container_resource: typing.Optional[
        kubernetes.client.V2beta2ContainerResourceMetricStatus
    ]
    external: typing.Optional[kubernetes.client.V2beta2ExternalMetricStatus]
    object: typing.Optional[kubernetes.client.V2beta2ObjectMetricStatus]
    pods: typing.Optional[kubernetes.client.V2beta2PodsMetricStatus]
    resource: typing.Optional[kubernetes.client.V2beta2ResourceMetricStatus]
    type: str

    def __init__(
        self,
        *,
        container_resource: typing.Optional[
            kubernetes.client.V2beta2ContainerResourceMetricStatus
        ] = ...,
        external: typing.Optional[kubernetes.client.V2beta2ExternalMetricStatus] = ...,
        object: typing.Optional[kubernetes.client.V2beta2ObjectMetricStatus] = ...,
        pods: typing.Optional[kubernetes.client.V2beta2PodsMetricStatus] = ...,
        resource: typing.Optional[kubernetes.client.V2beta2ResourceMetricStatus] = ...,
        type: str
    ) -> None: ...
    def to_dict(self) -> V2beta2MetricStatusDict: ...

class V2beta2MetricStatusDict(typing.TypedDict, total=False):
    containerResource: typing.Optional[
        kubernetes.client.V2beta2ContainerResourceMetricStatusDict
    ]
    external: typing.Optional[kubernetes.client.V2beta2ExternalMetricStatusDict]
    object: typing.Optional[kubernetes.client.V2beta2ObjectMetricStatusDict]
    pods: typing.Optional[kubernetes.client.V2beta2PodsMetricStatusDict]
    resource: typing.Optional[kubernetes.client.V2beta2ResourceMetricStatusDict]
    type: str
