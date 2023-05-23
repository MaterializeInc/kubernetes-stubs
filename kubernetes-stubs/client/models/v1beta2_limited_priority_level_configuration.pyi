import datetime
import typing

import kubernetes.client

class V1beta2LimitedPriorityLevelConfiguration:
    assured_concurrency_shares: typing.Optional[int]
    borrowing_limit_percent: typing.Optional[int]
    lendable_percent: typing.Optional[int]
    limit_response: typing.Optional[kubernetes.client.V1beta2LimitResponse]
    def __init__(
        self,
        *,
        assured_concurrency_shares: typing.Optional[int] = ...,
        borrowing_limit_percent: typing.Optional[int] = ...,
        lendable_percent: typing.Optional[int] = ...,
        limit_response: typing.Optional[kubernetes.client.V1beta2LimitResponse] = ...
    ) -> None: ...
    def to_dict(self) -> V1beta2LimitedPriorityLevelConfigurationDict: ...

class V1beta2LimitedPriorityLevelConfigurationDict(typing.TypedDict, total=False):
    assuredConcurrencyShares: typing.Optional[int]
    borrowingLimitPercent: typing.Optional[int]
    lendablePercent: typing.Optional[int]
    limitResponse: typing.Optional[kubernetes.client.V1beta2LimitResponseDict]
