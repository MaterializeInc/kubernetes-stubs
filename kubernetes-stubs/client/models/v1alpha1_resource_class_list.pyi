import datetime
import typing

import kubernetes.client

class V1alpha1ResourceClassList:
    api_version: typing.Optional[str]
    items: list[kubernetes.client.V1alpha1ResourceClass]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes.client.V1ListMeta]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        items: list[kubernetes.client.V1alpha1ResourceClass],
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes.client.V1ListMeta] = ...
    ) -> None: ...
    def to_dict(self) -> V1alpha1ResourceClassListDict: ...

class V1alpha1ResourceClassListDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    items: list[kubernetes.client.V1alpha1ResourceClassDict]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes.client.V1ListMetaDict]
