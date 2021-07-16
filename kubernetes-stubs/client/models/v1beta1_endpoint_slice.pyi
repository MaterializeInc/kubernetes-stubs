import datetime
import typing

import kubernetes.client

class V1beta1EndpointSlice:
    address_type: str
    api_version: typing.Optional[str]
    endpoints: list[kubernetes.client.V1beta1Endpoint]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes.client.V1ObjectMeta]
    ports: typing.Optional[list[kubernetes.client.V1beta1EndpointPort]]
    def __init__(
        self,
        *,
        address_type: str,
        api_version: typing.Optional[str] = ...,
        endpoints: list[kubernetes.client.V1beta1Endpoint],
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes.client.V1ObjectMeta] = ...,
        ports: typing.Optional[list[kubernetes.client.V1beta1EndpointPort]] = ...
    ) -> None: ...
