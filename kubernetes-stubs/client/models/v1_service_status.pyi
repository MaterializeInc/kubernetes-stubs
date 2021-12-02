import datetime
import typing

import kubernetes.client

class V1ServiceStatus:
    conditions: typing.Optional[list[kubernetes.client.V1Condition]]
    load_balancer: typing.Optional[kubernetes.client.V1LoadBalancerStatus]
    def __init__(
        self,
        *,
        conditions: typing.Optional[list[kubernetes.client.V1Condition]] = ...,
        load_balancer: typing.Optional[kubernetes.client.V1LoadBalancerStatus] = ...
    ) -> None: ...
    def to_dict(self) -> V1ServiceStatusDict: ...

class V1ServiceStatusDict(typing.TypedDict, total=False):
    conditions: typing.Optional[list[kubernetes.client.V1ConditionDict]]
    loadBalancer: typing.Optional[kubernetes.client.V1LoadBalancerStatusDict]
