import datetime
import typing

import kubernetes.client

class V1IngressLoadBalancerIngress:
    hostname: typing.Optional[str]
    ip: typing.Optional[str]
    ports: typing.Optional[list[kubernetes.client.V1IngressPortStatus]]
    def __init__(
        self,
        *,
        hostname: typing.Optional[str] = ...,
        ip: typing.Optional[str] = ...,
        ports: typing.Optional[list[kubernetes.client.V1IngressPortStatus]] = ...
    ) -> None: ...
    def to_dict(self) -> V1IngressLoadBalancerIngressDict: ...

class V1IngressLoadBalancerIngressDict(typing.TypedDict, total=False):
    hostname: typing.Optional[str]
    ip: typing.Optional[str]
    ports: typing.Optional[list[kubernetes.client.V1IngressPortStatusDict]]
