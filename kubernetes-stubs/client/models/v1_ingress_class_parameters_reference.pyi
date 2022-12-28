import datetime
import typing

import kubernetes.client

class V1IngressClassParametersReference:
    api_group: typing.Optional[str]
    kind: str
    name: str
    namespace: typing.Optional[str]
    scope: typing.Optional[str]

    def __init__(
        self,
        *,
        api_group: typing.Optional[str] = ...,
        kind: str,
        name: str,
        namespace: typing.Optional[str] = ...,
        scope: typing.Optional[str] = ...
    ) -> None: ...
    def to_dict(self) -> V1IngressClassParametersReferenceDict: ...

class V1IngressClassParametersReferenceDict(typing.TypedDict, total=False):
    apiGroup: typing.Optional[str]
    kind: str
    name: str
    namespace: typing.Optional[str]
    scope: typing.Optional[str]
