import datetime
import typing

import kubernetes.client

class V1LocalVolumeSource:
    fs_type: typing.Optional[str]
    path: str
    def __init__(self, *, fs_type: typing.Optional[str] = ..., path: str) -> None: ...
