import datetime
import typing

import kubernetes.client

class V1beta2FlowSchema:
    api_version: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes.client.V1ObjectMeta]
    spec: typing.Optional[kubernetes.client.V1beta2FlowSchemaSpec]
    status: typing.Optional[kubernetes.client.V1beta2FlowSchemaStatus]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes.client.V1ObjectMeta] = ...,
        spec: typing.Optional[kubernetes.client.V1beta2FlowSchemaSpec] = ...,
        status: typing.Optional[kubernetes.client.V1beta2FlowSchemaStatus] = ...
    ) -> None: ...
    def to_dict(self) -> V1beta2FlowSchemaDict: ...

class V1beta2FlowSchemaDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes.client.V1ObjectMetaDict]
    spec: typing.Optional[kubernetes.client.V1beta2FlowSchemaSpecDict]
    status: typing.Optional[kubernetes.client.V1beta2FlowSchemaStatusDict]
