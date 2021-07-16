import datetime
import typing

import kubernetes.client

class V1KeyToPath:
    key: str
    mode: typing.Optional[int]
    path: str
    def __init__(
        self, *, key: str, mode: typing.Optional[int] = ..., path: str
    ) -> None: ...
