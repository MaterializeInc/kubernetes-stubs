import datetime
import typing

import kubernetes.client

class V1beta3UserSubject:
    name: str
    def __init__(self, *, name: str) -> None: ...
    def to_dict(self) -> V1beta3UserSubjectDict: ...

class V1beta3UserSubjectDict(typing.TypedDict, total=False):
    name: str
