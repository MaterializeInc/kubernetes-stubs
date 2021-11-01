import datetime
import typing

import kubernetes.client

class V1CSIDriverSpec:
    attach_required: typing.Optional[bool]
    fs_group_policy: typing.Optional[str]
    pod_info_on_mount: typing.Optional[bool]
    storage_capacity: typing.Optional[bool]
    volume_lifecycle_modes: typing.Optional[list[str]]
    def __init__(
        self,
        *,
        attach_required: typing.Optional[bool] = ...,
        fs_group_policy: typing.Optional[str] = ...,
        pod_info_on_mount: typing.Optional[bool] = ...,
        storage_capacity: typing.Optional[bool] = ...,
        volume_lifecycle_modes: typing.Optional[list[str]] = ...
    ) -> None: ...
    def to_dict(self) -> V1CSIDriverSpecDict: ...

class V1CSIDriverSpecDict(typing.TypedDict, total=False):
    attachRequired: typing.Optional[bool]
    fsGroupPolicy: typing.Optional[str]
    podInfoOnMount: typing.Optional[bool]
    storageCapacity: typing.Optional[bool]
    volumeLifecycleModes: typing.Optional[list[str]]
