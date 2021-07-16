import datetime
import typing

import kubernetes.client

class V1HorizontalPodAutoscaler:
    api_version: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes.client.V1ObjectMeta]
    spec: typing.Optional[kubernetes.client.V1HorizontalPodAutoscalerSpec]
    status: typing.Optional[kubernetes.client.V1HorizontalPodAutoscalerStatus]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes.client.V1ObjectMeta] = ...,
        spec: typing.Optional[kubernetes.client.V1HorizontalPodAutoscalerSpec] = ...,
        status: typing.Optional[kubernetes.client.V1HorizontalPodAutoscalerStatus] = ...
    ) -> None: ...
