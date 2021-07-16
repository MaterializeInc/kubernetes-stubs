import datetime
import typing

import kubernetes.client

class ExtensionsV1beta1RunAsUserStrategyOptions:
    ranges: typing.Optional[list[kubernetes.client.ExtensionsV1beta1IDRange]]
    rule: str
    def __init__(
        self,
        *,
        ranges: typing.Optional[list[kubernetes.client.ExtensionsV1beta1IDRange]] = ...,
        rule: str
    ) -> None: ...
