import datetime
import typing

import kubernetes.client

class V1alpha1PodScheduling:
    api_version: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes.client.V1ObjectMeta]
    spec: kubernetes.client.V1alpha1PodSchedulingSpec
    status: typing.Optional[kubernetes.client.V1alpha1PodSchedulingStatus]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes.client.V1ObjectMeta] = ...,
        spec: kubernetes.client.V1alpha1PodSchedulingSpec,
        status: typing.Optional[kubernetes.client.V1alpha1PodSchedulingStatus] = ...
    ) -> None: ...
    def to_dict(self) -> V1alpha1PodSchedulingDict: ...

class V1alpha1PodSchedulingDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes.client.V1ObjectMetaDict]
    spec: kubernetes.client.V1alpha1PodSchedulingSpecDict
    status: typing.Optional[kubernetes.client.V1alpha1PodSchedulingStatusDict]
