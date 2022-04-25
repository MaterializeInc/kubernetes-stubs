import datetime
import typing

import kubernetes.client

class V2MetricStatus:
    container_resource: typing.Optional[
        kubernetes.client.V2ContainerResourceMetricStatus
    ]
    external: typing.Optional[kubernetes.client.V2ExternalMetricStatus]
    object: typing.Optional[kubernetes.client.V2ObjectMetricStatus]
    pods: typing.Optional[kubernetes.client.V2PodsMetricStatus]
    resource: typing.Optional[kubernetes.client.V2ResourceMetricStatus]
    type: str
    def __init__(
        self,
        *,
        container_resource: typing.Optional[
            kubernetes.client.V2ContainerResourceMetricStatus
        ] = ...,
        external: typing.Optional[kubernetes.client.V2ExternalMetricStatus] = ...,
        object: typing.Optional[kubernetes.client.V2ObjectMetricStatus] = ...,
        pods: typing.Optional[kubernetes.client.V2PodsMetricStatus] = ...,
        resource: typing.Optional[kubernetes.client.V2ResourceMetricStatus] = ...,
        type: str
    ) -> None: ...
    def to_dict(self) -> V2MetricStatusDict: ...

class V2MetricStatusDict(typing.TypedDict, total=False):
    containerResource: typing.Optional[
        kubernetes.client.V2ContainerResourceMetricStatusDict
    ]
    external: typing.Optional[kubernetes.client.V2ExternalMetricStatusDict]
    object: typing.Optional[kubernetes.client.V2ObjectMetricStatusDict]
    pods: typing.Optional[kubernetes.client.V2PodsMetricStatusDict]
    resource: typing.Optional[kubernetes.client.V2ResourceMetricStatusDict]
    type: str
