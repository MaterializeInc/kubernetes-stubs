import datetime
import typing

import kubernetes.client

class V1beta1PriorityLevelConfigurationReference:
    name: str

    def __init__(self, *, name: str) -> None: ...
    def to_dict(self) -> V1beta1PriorityLevelConfigurationReferenceDict: ...

class V1beta1PriorityLevelConfigurationReferenceDict(typing.TypedDict, total=False):
    name: str
