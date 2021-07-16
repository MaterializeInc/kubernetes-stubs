import datetime
import typing

import kubernetes.client

class V1FCVolumeSource:
    fs_type: typing.Optional[str]
    lun: typing.Optional[int]
    read_only: typing.Optional[bool]
    target_ww_ns: typing.Optional[list[str]]
    wwids: typing.Optional[list[str]]
    def __init__(
        self,
        *,
        fs_type: typing.Optional[str] = ...,
        lun: typing.Optional[int] = ...,
        read_only: typing.Optional[bool] = ...,
        target_ww_ns: typing.Optional[list[str]] = ...,
        wwids: typing.Optional[list[str]] = ...
    ) -> None: ...
