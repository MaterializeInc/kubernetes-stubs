import datetime
import typing

import kubernetes.client

class V1alpha1Validation:
    expression: str
    message: typing.Optional[str]
    reason: typing.Optional[str]
    def __init__(
        self,
        *,
        expression: str,
        message: typing.Optional[str] = ...,
        reason: typing.Optional[str] = ...
    ) -> None: ...
    def to_dict(self) -> V1alpha1ValidationDict: ...

class V1alpha1ValidationDict(typing.TypedDict, total=False):
    expression: str
    message: typing.Optional[str]
    reason: typing.Optional[str]
