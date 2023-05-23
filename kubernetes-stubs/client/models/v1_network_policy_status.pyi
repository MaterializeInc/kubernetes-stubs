import datetime
import typing

import kubernetes.client

class V1NetworkPolicyStatus:
    conditions: typing.Optional[list[kubernetes.client.V1Condition]]
    def __init__(
        self, *, conditions: typing.Optional[list[kubernetes.client.V1Condition]] = ...
    ) -> None: ...
    def to_dict(self) -> V1NetworkPolicyStatusDict: ...

class V1NetworkPolicyStatusDict(typing.TypedDict, total=False):
    conditions: typing.Optional[list[kubernetes.client.V1ConditionDict]]
