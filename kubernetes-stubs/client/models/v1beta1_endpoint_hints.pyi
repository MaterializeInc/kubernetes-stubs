import datetime
import typing

import kubernetes.client

class V1beta1EndpointHints:
    for_zones: typing.Optional[list[kubernetes.client.V1beta1ForZone]]
    def __init__(
        self,
        *,
        for_zones: typing.Optional[list[kubernetes.client.V1beta1ForZone]] = ...
    ) -> None: ...
    def to_dict(self) -> V1beta1EndpointHintsDict: ...

class V1beta1EndpointHintsDict(typing.TypedDict, total=False):
    forZones: typing.Optional[list[kubernetes.client.V1beta1ForZoneDict]]
