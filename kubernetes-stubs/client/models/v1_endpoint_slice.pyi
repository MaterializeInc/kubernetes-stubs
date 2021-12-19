import datetime
import typing

import kubernetes.client

class V1EndpointSlice:
    address_type: str
    api_version: typing.Optional[str]
    endpoints: list[kubernetes.client.V1Endpoint]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes.client.V1ObjectMeta]
    ports: typing.Optional[list[kubernetes.client.DiscoveryV1EndpointPort]]
    def __init__(
        self,
        *,
        address_type: str,
        api_version: typing.Optional[str] = ...,
        endpoints: list[kubernetes.client.V1Endpoint],
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes.client.V1ObjectMeta] = ...,
        ports: typing.Optional[list[kubernetes.client.DiscoveryV1EndpointPort]] = ...
    ) -> None: ...
    def to_dict(self) -> V1EndpointSliceDict: ...

class V1EndpointSliceDict(typing.TypedDict, total=False):
    addressType: str
    apiVersion: typing.Optional[str]
    endpoints: list[kubernetes.client.V1EndpointDict]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes.client.V1ObjectMetaDict]
    ports: typing.Optional[list[kubernetes.client.DiscoveryV1EndpointPortDict]]
