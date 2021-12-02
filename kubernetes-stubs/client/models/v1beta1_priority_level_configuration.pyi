import datetime
import typing

import kubernetes.client

class V1beta1PriorityLevelConfiguration:
    api_version: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes.client.V1ObjectMeta]
    spec: typing.Optional[kubernetes.client.V1beta1PriorityLevelConfigurationSpec]
    status: typing.Optional[kubernetes.client.V1beta1PriorityLevelConfigurationStatus]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes.client.V1ObjectMeta] = ...,
        spec: typing.Optional[
            kubernetes.client.V1beta1PriorityLevelConfigurationSpec
        ] = ...,
        status: typing.Optional[
            kubernetes.client.V1beta1PriorityLevelConfigurationStatus
        ] = ...
    ) -> None: ...
    def to_dict(self) -> V1beta1PriorityLevelConfigurationDict: ...

class V1beta1PriorityLevelConfigurationDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes.client.V1ObjectMetaDict]
    spec: typing.Optional[kubernetes.client.V1beta1PriorityLevelConfigurationSpecDict]
    status: typing.Optional[
        kubernetes.client.V1beta1PriorityLevelConfigurationStatusDict
    ]
