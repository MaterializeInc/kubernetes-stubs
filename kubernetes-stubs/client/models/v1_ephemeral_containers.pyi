import datetime
import typing

import kubernetes.client

class V1EphemeralContainers:
    api_version: typing.Optional[str]
    ephemeral_containers: list[kubernetes.client.V1EphemeralContainer]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes.client.V1ObjectMeta]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        ephemeral_containers: list[kubernetes.client.V1EphemeralContainer],
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes.client.V1ObjectMeta] = ...
    ) -> None: ...
    def to_dict(self) -> V1EphemeralContainersDict: ...

class V1EphemeralContainersDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    ephemeralContainers: list[kubernetes.client.V1EphemeralContainerDict]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes.client.V1ObjectMetaDict]
