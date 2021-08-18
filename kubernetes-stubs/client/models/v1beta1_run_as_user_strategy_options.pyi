import datetime
import typing

import kubernetes.client

class V1beta1RunAsUserStrategyOptions:
    ranges: typing.Optional[list[kubernetes.client.V1beta1IDRange]]
    rule: str
    def __init__(
        self,
        *,
        ranges: typing.Optional[list[kubernetes.client.V1beta1IDRange]] = ...,
        rule: str
    ) -> None: ...
