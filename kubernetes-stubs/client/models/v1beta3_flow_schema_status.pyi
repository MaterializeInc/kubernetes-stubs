import datetime
import typing

import kubernetes.client

class V1beta3FlowSchemaStatus:
    conditions: typing.Optional[list[kubernetes.client.V1beta3FlowSchemaCondition]]
    def __init__(
        self,
        *,
        conditions: typing.Optional[
            list[kubernetes.client.V1beta3FlowSchemaCondition]
        ] = ...
    ) -> None: ...
    def to_dict(self) -> V1beta3FlowSchemaStatusDict: ...

class V1beta3FlowSchemaStatusDict(typing.TypedDict, total=False):
    conditions: typing.Optional[list[kubernetes.client.V1beta3FlowSchemaConditionDict]]
