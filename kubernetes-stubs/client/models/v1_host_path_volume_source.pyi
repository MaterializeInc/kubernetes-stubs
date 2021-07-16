import datetime
import typing

import kubernetes.client

class V1HostPathVolumeSource:
    path: str
    type: typing.Optional[str]
    def __init__(self, *, path: str, type: typing.Optional[str] = ...) -> None: ...
