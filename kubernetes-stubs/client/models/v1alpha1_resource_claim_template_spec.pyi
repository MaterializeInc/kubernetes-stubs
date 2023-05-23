import datetime
import typing

import kubernetes.client

class V1alpha1ResourceClaimTemplateSpec:
    metadata: typing.Optional[kubernetes.client.V1ObjectMeta]
    spec: kubernetes.client.V1alpha1ResourceClaimSpec
    def __init__(
        self,
        *,
        metadata: typing.Optional[kubernetes.client.V1ObjectMeta] = ...,
        spec: kubernetes.client.V1alpha1ResourceClaimSpec
    ) -> None: ...
    def to_dict(self) -> V1alpha1ResourceClaimTemplateSpecDict: ...

class V1alpha1ResourceClaimTemplateSpecDict(typing.TypedDict, total=False):
    metadata: typing.Optional[kubernetes.client.V1ObjectMetaDict]
    spec: kubernetes.client.V1alpha1ResourceClaimSpecDict
