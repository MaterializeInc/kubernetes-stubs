import datetime
import typing

import kubernetes.client

class V2beta2MetricSpec:
    container_resource: typing.Optional[
        kubernetes.client.V2beta2ContainerResourceMetricSource
    ]
    external: typing.Optional[kubernetes.client.V2beta2ExternalMetricSource]
    object: typing.Optional[kubernetes.client.V2beta2ObjectMetricSource]
    pods: typing.Optional[kubernetes.client.V2beta2PodsMetricSource]
    resource: typing.Optional[kubernetes.client.V2beta2ResourceMetricSource]
    type: str

    def __init__(
        self,
        *,
        container_resource: typing.Optional[
            kubernetes.client.V2beta2ContainerResourceMetricSource
        ] = ...,
        external: typing.Optional[kubernetes.client.V2beta2ExternalMetricSource] = ...,
        object: typing.Optional[kubernetes.client.V2beta2ObjectMetricSource] = ...,
        pods: typing.Optional[kubernetes.client.V2beta2PodsMetricSource] = ...,
        resource: typing.Optional[kubernetes.client.V2beta2ResourceMetricSource] = ...,
        type: str
    ) -> None: ...
    def to_dict(self) -> V2beta2MetricSpecDict: ...

class V2beta2MetricSpecDict(typing.TypedDict, total=False):
    containerResource: typing.Optional[
        kubernetes.client.V2beta2ContainerResourceMetricSourceDict
    ]
    external: typing.Optional[kubernetes.client.V2beta2ExternalMetricSourceDict]
    object: typing.Optional[kubernetes.client.V2beta2ObjectMetricSourceDict]
    pods: typing.Optional[kubernetes.client.V2beta2PodsMetricSourceDict]
    resource: typing.Optional[kubernetes.client.V2beta2ResourceMetricSourceDict]
    type: str
