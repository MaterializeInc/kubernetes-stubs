import datetime
import typing

import kubernetes.client

class V1beta2PriorityLevelConfigurationReference:
    name: str
    def __init__(self, *, name: str) -> None: ...
    def to_dict(self) -> V1beta2PriorityLevelConfigurationReferenceDict: ...

class V1beta2PriorityLevelConfigurationReferenceDict(typing.TypedDict, total=False):
    name: str
