import datetime
import typing

import kubernetes.client

class V1NetworkPolicy:
    api_version: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes.client.V1ObjectMeta]
    spec: typing.Optional[kubernetes.client.V1NetworkPolicySpec]
    status: typing.Optional[kubernetes.client.V1NetworkPolicyStatus]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes.client.V1ObjectMeta] = ...,
        spec: typing.Optional[kubernetes.client.V1NetworkPolicySpec] = ...,
        status: typing.Optional[kubernetes.client.V1NetworkPolicyStatus] = ...
    ) -> None: ...
    def to_dict(self) -> V1NetworkPolicyDict: ...

class V1NetworkPolicyDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes.client.V1ObjectMetaDict]
    spec: typing.Optional[kubernetes.client.V1NetworkPolicySpecDict]
    status: typing.Optional[kubernetes.client.V1NetworkPolicyStatusDict]
