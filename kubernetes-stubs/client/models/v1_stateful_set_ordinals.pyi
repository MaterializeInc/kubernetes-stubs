import datetime
import typing

import kubernetes.client

class V1StatefulSetOrdinals:
    start: typing.Optional[int]
    def __init__(self, *, start: typing.Optional[int] = ...) -> None: ...
    def to_dict(self) -> V1StatefulSetOrdinalsDict: ...

class V1StatefulSetOrdinalsDict(typing.TypedDict, total=False):
    start: typing.Optional[int]
