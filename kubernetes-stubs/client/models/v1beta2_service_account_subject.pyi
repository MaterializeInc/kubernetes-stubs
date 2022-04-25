import datetime
import typing

import kubernetes.client

class V1beta2ServiceAccountSubject:
    name: str
    namespace: str
    def __init__(self, *, name: str, namespace: str) -> None: ...
    def to_dict(self) -> V1beta2ServiceAccountSubjectDict: ...

class V1beta2ServiceAccountSubjectDict(typing.TypedDict, total=False):
    name: str
    namespace: str
