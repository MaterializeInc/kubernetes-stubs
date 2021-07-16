import datetime
import typing

import kubernetes.client

class V1BoundObjectReference:
    api_version: typing.Optional[str]
    kind: typing.Optional[str]
    name: typing.Optional[str]
    uid: typing.Optional[str]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        name: typing.Optional[str] = ...,
        uid: typing.Optional[str] = ...
    ) -> None: ...
