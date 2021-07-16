import datetime
import typing

import kubernetes.client

class V1beta2DeploymentCondition:
    last_transition_time: typing.Optional[datetime.datetime]
    last_update_time: typing.Optional[datetime.datetime]
    message: typing.Optional[str]
    reason: typing.Optional[str]
    status: str
    type: str
    def __init__(
        self,
        *,
        last_transition_time: typing.Optional[datetime.datetime] = ...,
        last_update_time: typing.Optional[datetime.datetime] = ...,
        message: typing.Optional[str] = ...,
        reason: typing.Optional[str] = ...,
        status: str,
        type: str
    ) -> None: ...
