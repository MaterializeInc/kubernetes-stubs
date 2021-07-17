import datetime
import typing

import kubernetes.client

class V1IPBlock:
    cidr: str
    _except: typing.Optional[list[str]]
    def __init__(
        self, *, cidr: str, _except: typing.Optional[list[str]] = ...
    ) -> None: ...
