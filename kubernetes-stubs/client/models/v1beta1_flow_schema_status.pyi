import datetime
import typing

import kubernetes.client

class V1beta1FlowSchemaStatus:
    conditions: typing.Optional[list[kubernetes.client.V1beta1FlowSchemaCondition]]

    def __init__(
        self,
        *,
        conditions: typing.Optional[
            list[kubernetes.client.V1beta1FlowSchemaCondition]
        ] = ...
    ) -> None: ...
    def to_dict(self) -> V1beta1FlowSchemaStatusDict: ...

class V1beta1FlowSchemaStatusDict(typing.TypedDict, total=False):
    conditions: typing.Optional[list[kubernetes.client.V1beta1FlowSchemaConditionDict]]
