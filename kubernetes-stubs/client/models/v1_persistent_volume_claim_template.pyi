import datetime
import typing

import kubernetes.client

class V1PersistentVolumeClaimTemplate:
    metadata: typing.Optional[kubernetes.client.V1ObjectMeta]
    spec: kubernetes.client.V1PersistentVolumeClaimSpec
    def __init__(
        self,
        *,
        metadata: typing.Optional[kubernetes.client.V1ObjectMeta] = ...,
        spec: kubernetes.client.V1PersistentVolumeClaimSpec
    ) -> None: ...
    def to_dict(self) -> V1PersistentVolumeClaimTemplateDict: ...

class V1PersistentVolumeClaimTemplateDict(typing.TypedDict, total=False):
    metadata: typing.Optional[kubernetes.client.V1ObjectMetaDict]
    spec: kubernetes.client.V1PersistentVolumeClaimSpecDict
