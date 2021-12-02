import datetime
import typing

import kubernetes.client

class V1beta1UserSubject:
    name: str
    def __init__(self, *, name: str) -> None: ...
    def to_dict(self) -> V1beta1UserSubjectDict: ...

class V1beta1UserSubjectDict(typing.TypedDict, total=False):
    name: str
