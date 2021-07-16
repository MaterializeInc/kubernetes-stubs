import datetime
import typing

import kubernetes.client

class V1StorageClass:
    allow_volume_expansion: typing.Optional[bool]
    allowed_topologies: typing.Optional[list[kubernetes.client.V1TopologySelectorTerm]]
    api_version: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes.client.V1ObjectMeta]
    mount_options: typing.Optional[list[str]]
    parameters: typing.Optional[dict[str, str]]
    provisioner: str
    reclaim_policy: typing.Optional[str]
    volume_binding_mode: typing.Optional[str]
    def __init__(
        self,
        *,
        allow_volume_expansion: typing.Optional[bool] = ...,
        allowed_topologies: typing.Optional[
            list[kubernetes.client.V1TopologySelectorTerm]
        ] = ...,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes.client.V1ObjectMeta] = ...,
        mount_options: typing.Optional[list[str]] = ...,
        parameters: typing.Optional[dict[str, str]] = ...,
        provisioner: str,
        reclaim_policy: typing.Optional[str] = ...,
        volume_binding_mode: typing.Optional[str] = ...
    ) -> None: ...
