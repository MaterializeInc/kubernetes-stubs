import datetime
import typing

import kubernetes.client

class V1PodOS:
    name: str
    def __init__(self, *, name: str) -> None: ...
    def to_dict(self) -> V1PodOSDict: ...

class V1PodOSDict(typing.TypedDict, total=False):
    name: str
