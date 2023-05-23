import datetime
import typing

import kubernetes.client

class V1beta3PriorityLevelConfigurationReference:
    name: str
    def __init__(self, *, name: str) -> None: ...
    def to_dict(self) -> V1beta3PriorityLevelConfigurationReferenceDict: ...

class V1beta3PriorityLevelConfigurationReferenceDict(typing.TypedDict, total=False):
    name: str
