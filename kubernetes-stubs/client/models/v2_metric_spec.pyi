import datetime
import typing

import kubernetes.client

class V2MetricSpec:
    container_resource: typing.Optional[
        kubernetes.client.V2ContainerResourceMetricSource
    ]
    external: typing.Optional[kubernetes.client.V2ExternalMetricSource]
    object: typing.Optional[kubernetes.client.V2ObjectMetricSource]
    pods: typing.Optional[kubernetes.client.V2PodsMetricSource]
    resource: typing.Optional[kubernetes.client.V2ResourceMetricSource]
    type: str
    def __init__(
        self,
        *,
        container_resource: typing.Optional[
            kubernetes.client.V2ContainerResourceMetricSource
        ] = ...,
        external: typing.Optional[kubernetes.client.V2ExternalMetricSource] = ...,
        object: typing.Optional[kubernetes.client.V2ObjectMetricSource] = ...,
        pods: typing.Optional[kubernetes.client.V2PodsMetricSource] = ...,
        resource: typing.Optional[kubernetes.client.V2ResourceMetricSource] = ...,
        type: str
    ) -> None: ...
    def to_dict(self) -> V2MetricSpecDict: ...

class V2MetricSpecDict(typing.TypedDict, total=False):
    containerResource: typing.Optional[
        kubernetes.client.V2ContainerResourceMetricSourceDict
    ]
    external: typing.Optional[kubernetes.client.V2ExternalMetricSourceDict]
    object: typing.Optional[kubernetes.client.V2ObjectMetricSourceDict]
    pods: typing.Optional[kubernetes.client.V2PodsMetricSourceDict]
    resource: typing.Optional[kubernetes.client.V2ResourceMetricSourceDict]
    type: str
