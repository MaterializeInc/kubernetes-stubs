import datetime
import typing

import kubernetes.client

class V1PortworxVolumeSource:
    fs_type: typing.Optional[str]
    read_only: typing.Optional[bool]
    volume_id: str
    def __init__(
        self,
        *,
        fs_type: typing.Optional[str] = ...,
        read_only: typing.Optional[bool] = ...,
        volume_id: str
    ) -> None: ...
