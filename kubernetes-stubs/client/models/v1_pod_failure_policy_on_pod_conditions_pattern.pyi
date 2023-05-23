import datetime
import typing

import kubernetes.client

class V1PodFailurePolicyOnPodConditionsPattern:
    status: str
    type: str
    def __init__(self, *, status: str, type: str) -> None: ...
    def to_dict(self) -> V1PodFailurePolicyOnPodConditionsPatternDict: ...

class V1PodFailurePolicyOnPodConditionsPatternDict(typing.TypedDict, total=False):
    status: str
    type: str
