import datetime
import typing

import kubernetes.client

class V1beta1CustomResourceColumnDefinition:
    json_path: str
    description: typing.Optional[str]
    format: typing.Optional[str]
    name: str
    priority: typing.Optional[int]
    type: str
    def __init__(
        self,
        *,
        json_path: str,
        description: typing.Optional[str] = ...,
        format: typing.Optional[str] = ...,
        name: str,
        priority: typing.Optional[int] = ...,
        type: str
    ) -> None: ...
