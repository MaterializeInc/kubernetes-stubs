import datetime
import typing

import kubernetes.client

class V1GCEPersistentDiskVolumeSource:
    fs_type: typing.Optional[str]
    partition: typing.Optional[int]
    pd_name: str
    read_only: typing.Optional[bool]
    def __init__(
        self,
        *,
        fs_type: typing.Optional[str] = ...,
        partition: typing.Optional[int] = ...,
        pd_name: str,
        read_only: typing.Optional[bool] = ...
    ) -> None: ...
