import datetime
import typing

import kubernetes.client

class V1alpha1PriorityLevelConfiguration:
    api_version: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes.client.V1ObjectMeta]
    spec: typing.Optional[kubernetes.client.V1alpha1PriorityLevelConfigurationSpec]
    status: typing.Optional[kubernetes.client.V1alpha1PriorityLevelConfigurationStatus]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes.client.V1ObjectMeta] = ...,
        spec: typing.Optional[
            kubernetes.client.V1alpha1PriorityLevelConfigurationSpec
        ] = ...,
        status: typing.Optional[
            kubernetes.client.V1alpha1PriorityLevelConfigurationStatus
        ] = ...
    ) -> None: ...
