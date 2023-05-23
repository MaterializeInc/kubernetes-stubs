import datetime
import typing

import kubernetes.client

class V1alpha1ParamRef:
    name: typing.Optional[str]
    namespace: typing.Optional[str]
    def __init__(
        self, *, name: typing.Optional[str] = ..., namespace: typing.Optional[str] = ...
    ) -> None: ...
    def to_dict(self) -> V1alpha1ParamRefDict: ...

class V1alpha1ParamRefDict(typing.TypedDict, total=False):
    name: typing.Optional[str]
    namespace: typing.Optional[str]
