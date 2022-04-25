import datetime
import typing

import kubernetes.client

class V1beta2UserSubject:
    name: str
    def __init__(self, *, name: str) -> None: ...
    def to_dict(self) -> V1beta2UserSubjectDict: ...

class V1beta2UserSubjectDict(typing.TypedDict, total=False):
    name: str
