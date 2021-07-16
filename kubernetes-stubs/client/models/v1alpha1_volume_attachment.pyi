import datetime
import typing

import kubernetes.client

class V1alpha1VolumeAttachment:
    api_version: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes.client.V1ObjectMeta]
    spec: kubernetes.client.V1alpha1VolumeAttachmentSpec
    status: typing.Optional[kubernetes.client.V1alpha1VolumeAttachmentStatus]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes.client.V1ObjectMeta] = ...,
        spec: kubernetes.client.V1alpha1VolumeAttachmentSpec,
        status: typing.Optional[kubernetes.client.V1alpha1VolumeAttachmentStatus] = ...
    ) -> None: ...
