import datetime
import typing

import kubernetes.client

class V1beta1SupplementalGroupsStrategyOptions:
    ranges: typing.Optional[list[kubernetes.client.V1beta1IDRange]]
    rule: typing.Optional[str]
    def __init__(
        self,
        *,
        ranges: typing.Optional[list[kubernetes.client.V1beta1IDRange]] = ...,
        rule: typing.Optional[str] = ...
    ) -> None: ...
