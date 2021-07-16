import datetime
import typing

import kubernetes.client

class V1alpha1FlowSchemaStatus:
    conditions: typing.Optional[list[kubernetes.client.V1alpha1FlowSchemaCondition]]
    def __init__(
        self,
        *,
        conditions: typing.Optional[
            list[kubernetes.client.V1alpha1FlowSchemaCondition]
        ] = ...
    ) -> None: ...
