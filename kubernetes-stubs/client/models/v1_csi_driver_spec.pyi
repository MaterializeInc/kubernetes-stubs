import datetime
import typing

import kubernetes.client

class V1CSIDriverSpec:
    attach_required: typing.Optional[bool]
    fs_group_policy: typing.Optional[str]
    pod_info_on_mount: typing.Optional[bool]
    requires_republish: typing.Optional[bool]
    se_linux_mount: typing.Optional[bool]
    storage_capacity: typing.Optional[bool]
    token_requests: typing.Optional[list[kubernetes.client.StorageV1TokenRequest]]
    volume_lifecycle_modes: typing.Optional[list[str]]
    def __init__(
        self,
        *,
        attach_required: typing.Optional[bool] = ...,
        fs_group_policy: typing.Optional[str] = ...,
        pod_info_on_mount: typing.Optional[bool] = ...,
        requires_republish: typing.Optional[bool] = ...,
        se_linux_mount: typing.Optional[bool] = ...,
        storage_capacity: typing.Optional[bool] = ...,
        token_requests: typing.Optional[
            list[kubernetes.client.StorageV1TokenRequest]
        ] = ...,
        volume_lifecycle_modes: typing.Optional[list[str]] = ...
    ) -> None: ...
    def to_dict(self) -> V1CSIDriverSpecDict: ...

class V1CSIDriverSpecDict(typing.TypedDict, total=False):
    attachRequired: typing.Optional[bool]
    fsGroupPolicy: typing.Optional[str]
    podInfoOnMount: typing.Optional[bool]
    requiresRepublish: typing.Optional[bool]
    seLinuxMount: typing.Optional[bool]
    storageCapacity: typing.Optional[bool]
    tokenRequests: typing.Optional[list[kubernetes.client.StorageV1TokenRequestDict]]
    volumeLifecycleModes: typing.Optional[list[str]]
