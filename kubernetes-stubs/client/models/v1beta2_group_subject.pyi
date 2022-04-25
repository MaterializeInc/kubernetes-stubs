import datetime
import typing

import kubernetes.client

class V1beta2GroupSubject:
    name: str
    def __init__(self, *, name: str) -> None: ...
    def to_dict(self) -> V1beta2GroupSubjectDict: ...

class V1beta2GroupSubjectDict(typing.TypedDict, total=False):
    name: str
