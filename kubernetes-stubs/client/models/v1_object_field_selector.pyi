import datetime
import typing

import kubernetes.client

class V1ObjectFieldSelector:
    api_version: typing.Optional[str]
    field_path: str
    def __init__(
        self, *, api_version: typing.Optional[str] = ..., field_path: str
    ) -> None: ...
