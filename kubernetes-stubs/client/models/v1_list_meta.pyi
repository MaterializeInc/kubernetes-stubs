import datetime
import typing

import kubernetes.client

class V1ListMeta:
    continue: typing.Optional[str]
    remaining_item_count: typing.Optional[int]
    resource_version: typing.Optional[str]
    self_link: typing.Optional[str]
    
    def __init__(self, *, continue: typing.Optional[str] = ..., remaining_item_count: typing.Optional[int] = ..., resource_version: typing.Optional[str] = ..., self_link: typing.Optional[str] = ...) -> None:
        ...
