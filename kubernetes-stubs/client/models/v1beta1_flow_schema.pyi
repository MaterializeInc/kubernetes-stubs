import datetime
import typing

import kubernetes.client

class V1beta1FlowSchema:
    api_version: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes.client.V1ObjectMeta]
    spec: typing.Optional[kubernetes.client.V1beta1FlowSchemaSpec]
    status: typing.Optional[kubernetes.client.V1beta1FlowSchemaStatus]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes.client.V1ObjectMeta] = ...,
        spec: typing.Optional[kubernetes.client.V1beta1FlowSchemaSpec] = ...,
        status: typing.Optional[kubernetes.client.V1beta1FlowSchemaStatus] = ...
    ) -> None: ...
    def to_dict(self) -> V1beta1FlowSchemaDict: ...

class V1beta1FlowSchemaDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes.client.V1ObjectMetaDict]
    spec: typing.Optional[kubernetes.client.V1beta1FlowSchemaSpecDict]
    status: typing.Optional[kubernetes.client.V1beta1FlowSchemaStatusDict]
