import datetime
import typing

import kubernetes.client

class V1PhotonPersistentDiskVolumeSource:
    fs_type: typing.Optional[str]
    pd_id: str
    def __init__(self, *, fs_type: typing.Optional[str] = ..., pd_id: str) -> None: ...
