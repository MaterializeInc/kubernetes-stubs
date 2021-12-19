import datetime
import typing

import kubernetes.client

class V1beta1IngressClassParametersReference:
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
    def to_dict(self) -> V1beta1IngressClassParametersReferenceDict: ...

class V1beta1IngressClassParametersReferenceDict(typing.TypedDict, total=False):
    apiGroup: typing.Optional[str]
    kind: str
    name: str
    namespace: typing.Optional[str]
    scope: typing.Optional[str]
