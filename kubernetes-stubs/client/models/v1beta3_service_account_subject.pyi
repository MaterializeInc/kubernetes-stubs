import datetime
import typing

import kubernetes.client

class V1beta3ServiceAccountSubject:
    name: str
    namespace: str
    def __init__(self, *, name: str, namespace: str) -> None: ...
    def to_dict(self) -> V1beta3ServiceAccountSubjectDict: ...

class V1beta3ServiceAccountSubjectDict(typing.TypedDict, total=False):
    name: str
    namespace: str
