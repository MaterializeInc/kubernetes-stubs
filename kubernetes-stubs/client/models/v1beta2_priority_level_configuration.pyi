import datetime
import typing

import kubernetes.client

class V1beta2PriorityLevelConfiguration:
    api_version: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes.client.V1ObjectMeta]
    spec: typing.Optional[kubernetes.client.V1beta2PriorityLevelConfigurationSpec]
    status: typing.Optional[kubernetes.client.V1beta2PriorityLevelConfigurationStatus]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes.client.V1ObjectMeta] = ...,
        spec: typing.Optional[
            kubernetes.client.V1beta2PriorityLevelConfigurationSpec
        ] = ...,
        status: typing.Optional[
            kubernetes.client.V1beta2PriorityLevelConfigurationStatus
        ] = ...
    ) -> None: ...
    def to_dict(self) -> V1beta2PriorityLevelConfigurationDict: ...

class V1beta2PriorityLevelConfigurationDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes.client.V1ObjectMetaDict]
    spec: typing.Optional[kubernetes.client.V1beta2PriorityLevelConfigurationSpecDict]
    status: typing.Optional[
        kubernetes.client.V1beta2PriorityLevelConfigurationStatusDict
    ]
