import datetime
import typing

import kubernetes.client

class V1beta3LimitedPriorityLevelConfiguration:
    borrowing_limit_percent: typing.Optional[int]
    lendable_percent: typing.Optional[int]
    limit_response: typing.Optional[kubernetes.client.V1beta3LimitResponse]
    nominal_concurrency_shares: typing.Optional[int]
    def __init__(
        self,
        *,
        borrowing_limit_percent: typing.Optional[int] = ...,
        lendable_percent: typing.Optional[int] = ...,
        limit_response: typing.Optional[kubernetes.client.V1beta3LimitResponse] = ...,
        nominal_concurrency_shares: typing.Optional[int] = ...
    ) -> None: ...
    def to_dict(self) -> V1beta3LimitedPriorityLevelConfigurationDict: ...

class V1beta3LimitedPriorityLevelConfigurationDict(typing.TypedDict, total=False):
    borrowingLimitPercent: typing.Optional[int]
    lendablePercent: typing.Optional[int]
    limitResponse: typing.Optional[kubernetes.client.V1beta3LimitResponseDict]
    nominalConcurrencyShares: typing.Optional[int]
