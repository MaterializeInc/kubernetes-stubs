import datetime
import typing

import kubernetes.client

class V1IngressStatus:
    load_balancer: typing.Optional[kubernetes.client.V1IngressLoadBalancerStatus]
    def __init__(
        self,
        *,
        load_balancer: typing.Optional[
            kubernetes.client.V1IngressLoadBalancerStatus
        ] = ...
    ) -> None: ...
    def to_dict(self) -> V1IngressStatusDict: ...

class V1IngressStatusDict(typing.TypedDict, total=False):
    loadBalancer: typing.Optional[kubernetes.client.V1IngressLoadBalancerStatusDict]
