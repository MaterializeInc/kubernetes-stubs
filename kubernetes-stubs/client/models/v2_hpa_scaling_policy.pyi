import datetime
import typing

import kubernetes.client

class V2HPAScalingPolicy:
    period_seconds: int
    type: str
    value: int
    def __init__(self, *, period_seconds: int, type: str, value: int) -> None: ...
    def to_dict(self) -> V2HPAScalingPolicyDict: ...

class V2HPAScalingPolicyDict(typing.TypedDict, total=False):
    periodSeconds: int
    type: str
    value: int
