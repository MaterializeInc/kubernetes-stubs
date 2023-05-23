import datetime
import typing

import kubernetes.client

class V1ValidationRule:
    message: typing.Optional[str]
    rule: str
    def __init__(self, *, message: typing.Optional[str] = ..., rule: str) -> None: ...
    def to_dict(self) -> V1ValidationRuleDict: ...

class V1ValidationRuleDict(typing.TypedDict, total=False):
    message: typing.Optional[str]
    rule: str
