import datetime
import typing

import kubernetes.client

class V1beta1GroupSubject:
    name: str
    def __init__(self, *, name: str) -> None: ...
    def to_dict(self) -> V1beta1GroupSubjectDict: ...

class V1beta1GroupSubjectDict(typing.TypedDict, total=False):
    name: str
