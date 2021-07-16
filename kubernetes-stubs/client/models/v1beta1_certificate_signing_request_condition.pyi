import datetime
import typing

import kubernetes.client

class V1beta1CertificateSigningRequestCondition:
    last_update_time: typing.Optional[datetime.datetime]
    message: typing.Optional[str]
    reason: typing.Optional[str]
    type: str
    def __init__(
        self,
        *,
        last_update_time: typing.Optional[datetime.datetime] = ...,
        message: typing.Optional[str] = ...,
        reason: typing.Optional[str] = ...,
        type: str
    ) -> None: ...
