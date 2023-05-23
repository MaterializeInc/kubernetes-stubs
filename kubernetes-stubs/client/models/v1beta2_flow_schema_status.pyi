import datetime
import typing

import kubernetes.client

class V1beta2FlowSchemaStatus:
    conditions: typing.Optional[list[kubernetes.client.V1beta2FlowSchemaCondition]]
    def __init__(
        self,
        *,
        conditions: typing.Optional[
            list[kubernetes.client.V1beta2FlowSchemaCondition]
        ] = ...
    ) -> None: ...
    def to_dict(self) -> V1beta2FlowSchemaStatusDict: ...

class V1beta2FlowSchemaStatusDict(typing.TypedDict, total=False):
    conditions: typing.Optional[list[kubernetes.client.V1beta2FlowSchemaConditionDict]]
