import datetime
import typing

import kubernetes.client

class V1TCPSocketAction:
    host: typing.Optional[str]
    port: typing.Any
    def __init__(
        self, *, host: typing.Optional[str] = ..., port: typing.Any
    ) -> None: ...
