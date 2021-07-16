import datetime
import typing

import kubernetes.client

class V1beta1Endpoint:
    addresses: list[str]
    conditions: typing.Optional[kubernetes.client.V1beta1EndpointConditions]
    hostname: typing.Optional[str]
    target_ref: typing.Optional[kubernetes.client.V1ObjectReference]
    topology: typing.Optional[dict[str, str]]
    def __init__(
        self,
        *,
        addresses: list[str],
        conditions: typing.Optional[kubernetes.client.V1beta1EndpointConditions] = ...,
        hostname: typing.Optional[str] = ...,
        target_ref: typing.Optional[kubernetes.client.V1ObjectReference] = ...,
        topology: typing.Optional[dict[str, str]] = ...
    ) -> None: ...
