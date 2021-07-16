import datetime
import typing

import kubernetes.client

class V1alpha1FlowSchemaCondition:
    last_transition_time: typing.Optional[datetime.datetime]
    message: typing.Optional[str]
    reason: typing.Optional[str]
    status: typing.Optional[str]
    type: typing.Optional[str]
    def __init__(
        self,
        *,
        last_transition_time: typing.Optional[datetime.datetime] = ...,
        message: typing.Optional[str] = ...,
        reason: typing.Optional[str] = ...,
        status: typing.Optional[str] = ...,
        type: typing.Optional[str] = ...
    ) -> None: ...
