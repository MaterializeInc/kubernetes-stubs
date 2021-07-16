import datetime
import typing

import kubernetes.client

class V1LocalObjectReference:
    name: typing.Optional[str]
    def __init__(self, *, name: typing.Optional[str] = ...) -> None: ...
