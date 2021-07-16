import datetime
import typing

import kubernetes.client

class V1ScaleStatus:
    replicas: int
    selector: typing.Optional[str]
    def __init__(
        self, *, replicas: int, selector: typing.Optional[str] = ...
    ) -> None: ...
