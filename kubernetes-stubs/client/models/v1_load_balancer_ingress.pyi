import datetime
import typing

import kubernetes.client

class V1LoadBalancerIngress:
    hostname: typing.Optional[str]
    ip: typing.Optional[str]
    ports: typing.Optional[list[kubernetes.client.V1PortStatus]]
    def __init__(
        self,
        *,
        hostname: typing.Optional[str] = ...,
        ip: typing.Optional[str] = ...,
        ports: typing.Optional[list[kubernetes.client.V1PortStatus]] = ...
    ) -> None: ...
    def to_dict(self) -> V1LoadBalancerIngressDict: ...

class V1LoadBalancerIngressDict(typing.TypedDict, total=False):
    hostname: typing.Optional[str]
    ip: typing.Optional[str]
    ports: typing.Optional[list[kubernetes.client.V1PortStatusDict]]
