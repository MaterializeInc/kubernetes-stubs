import datetime
import typing

import kubernetes.client

class V2MetricIdentifier:
    name: str
    selector: typing.Optional[kubernetes.client.V1LabelSelector]
    def __init__(
        self,
        *,
        name: str,
        selector: typing.Optional[kubernetes.client.V1LabelSelector] = ...
    ) -> None: ...
    def to_dict(self) -> V2MetricIdentifierDict: ...

class V2MetricIdentifierDict(typing.TypedDict, total=False):
    name: str
    selector: typing.Optional[kubernetes.client.V1LabelSelectorDict]
