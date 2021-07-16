import datetime
import typing

import kubernetes.client

class PolicyV1beta1SupplementalGroupsStrategyOptions:
    ranges: typing.Optional[list[kubernetes.client.PolicyV1beta1IDRange]]
    rule: typing.Optional[str]
    def __init__(
        self,
        *,
        ranges: typing.Optional[list[kubernetes.client.PolicyV1beta1IDRange]] = ...,
        rule: typing.Optional[str] = ...
    ) -> None: ...
