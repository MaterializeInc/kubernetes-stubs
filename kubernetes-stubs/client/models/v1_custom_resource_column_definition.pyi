import datetime
import typing

import kubernetes.client

class V1CustomResourceColumnDefinition:
    description: typing.Optional[str]
    format: typing.Optional[str]
    json_path: str
    name: str
    priority: typing.Optional[int]
    type: str
    def __init__(
        self,
        *,
        description: typing.Optional[str] = ...,
        format: typing.Optional[str] = ...,
        json_path: str,
        name: str,
        priority: typing.Optional[int] = ...,
        type: str
    ) -> None: ...
