import datetime
import typing

import kubernetes.client

class V1GlusterfsVolumeSource:
    endpoints: str
    path: str
    read_only: typing.Optional[bool]
    def __init__(
        self, *, endpoints: str, path: str, read_only: typing.Optional[bool] = ...
    ) -> None: ...
