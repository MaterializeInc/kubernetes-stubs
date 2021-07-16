import datetime
import typing

import kubernetes.client

class V1beta1SubjectAccessReviewStatus:
    allowed: bool
    denied: typing.Optional[bool]
    evaluation_error: typing.Optional[str]
    reason: typing.Optional[str]
    def __init__(
        self,
        *,
        allowed: bool,
        denied: typing.Optional[bool] = ...,
        evaluation_error: typing.Optional[str] = ...,
        reason: typing.Optional[str] = ...
    ) -> None: ...
