import datetime
import typing

import kubernetes.client

class V1ExecAction:
    command: typing.Optional[list[str]]
    def __init__(self, *, command: typing.Optional[list[str]] = ...) -> None: ...
