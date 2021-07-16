import datetime
import typing

import kubernetes.client

class V1SecretReference:
    name: typing.Optional[str]
    namespace: typing.Optional[str]
    def __init__(
        self, *, name: typing.Optional[str] = ..., namespace: typing.Optional[str] = ...
    ) -> None: ...
