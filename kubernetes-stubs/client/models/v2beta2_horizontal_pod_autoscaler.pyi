import datetime
import typing

import kubernetes.client

class V2beta2HorizontalPodAutoscaler:
    api_version: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes.client.V1ObjectMeta]
    spec: typing.Optional[kubernetes.client.V2beta2HorizontalPodAutoscalerSpec]
    status: typing.Optional[kubernetes.client.V2beta2HorizontalPodAutoscalerStatus]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes.client.V1ObjectMeta] = ...,
        spec: typing.Optional[
            kubernetes.client.V2beta2HorizontalPodAutoscalerSpec
        ] = ...,
        status: typing.Optional[
            kubernetes.client.V2beta2HorizontalPodAutoscalerStatus
        ] = ...
    ) -> None: ...
