import datetime
import typing

import kubernetes.client

class V1alpha1LimitedPriorityLevelConfiguration:
    assured_concurrency_shares: typing.Optional[int]
    limit_response: typing.Optional[kubernetes.client.V1alpha1LimitResponse]
    def __init__(
        self,
        *,
        assured_concurrency_shares: typing.Optional[int] = ...,
        limit_response: typing.Optional[kubernetes.client.V1alpha1LimitResponse] = ...
    ) -> None: ...
