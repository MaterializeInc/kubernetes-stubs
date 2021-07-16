import datetime
import typing

import kubernetes.client

class ExtensionsV1beta1FSGroupStrategyOptions:
    ranges: typing.Optional[list[kubernetes.client.ExtensionsV1beta1IDRange]]
    rule: typing.Optional[str]
    def __init__(
        self,
        *,
        ranges: typing.Optional[list[kubernetes.client.ExtensionsV1beta1IDRange]] = ...,
        rule: typing.Optional[str] = ...
    ) -> None: ...
