import datetime
import typing

import kubernetes.client

class V1PodIP:
    ip: typing.Optional[str]
    def __init__(self, *, ip: typing.Optional[str] = ...) -> None: ...
