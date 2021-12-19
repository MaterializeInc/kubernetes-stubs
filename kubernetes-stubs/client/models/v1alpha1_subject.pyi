import datetime
import typing

import kubernetes.client

class V1alpha1Subject:
    api_version: typing.Optional[str]
    kind: str
    name: str
    namespace: typing.Optional[str]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: str,
        name: str,
        namespace: typing.Optional[str] = ...
    ) -> None: ...
    def to_dict(self) -> V1alpha1SubjectDict: ...

class V1alpha1SubjectDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    kind: str
    name: str
    namespace: typing.Optional[str]
