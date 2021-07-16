import datetime
import typing

import kubernetes.client

class V1EndpointSubset:
    addresses: typing.Optional[list[kubernetes.client.V1EndpointAddress]]
    not_ready_addresses: typing.Optional[list[kubernetes.client.V1EndpointAddress]]
    ports: typing.Optional[list[kubernetes.client.V1EndpointPort]]
    def __init__(
        self,
        *,
        addresses: typing.Optional[list[kubernetes.client.V1EndpointAddress]] = ...,
        not_ready_addresses: typing.Optional[
            list[kubernetes.client.V1EndpointAddress]
        ] = ...,
        ports: typing.Optional[list[kubernetes.client.V1EndpointPort]] = ...
    ) -> None: ...
