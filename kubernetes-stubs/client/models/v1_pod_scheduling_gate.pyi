import datetime
import typing

import kubernetes.client

class V1PodSchedulingGate:
    name: str
    def __init__(self, *, name: str) -> None: ...
    def to_dict(self) -> V1PodSchedulingGateDict: ...

class V1PodSchedulingGateDict(typing.TypedDict, total=False):
    name: str
