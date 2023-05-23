import datetime
import typing

import kubernetes.client

class V1beta3GroupSubject:
    name: str
    def __init__(self, *, name: str) -> None: ...
    def to_dict(self) -> V1beta3GroupSubjectDict: ...

class V1beta3GroupSubjectDict(typing.TypedDict, total=False):
    name: str
