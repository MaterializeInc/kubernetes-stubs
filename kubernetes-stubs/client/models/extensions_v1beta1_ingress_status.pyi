import datetime
import typing

import kubernetes.client

class ExtensionsV1beta1IngressStatus:
    load_balancer: typing.Optional[kubernetes.client.V1LoadBalancerStatus]
    def __init__(
        self,
        *,
        load_balancer: typing.Optional[kubernetes.client.V1LoadBalancerStatus] = ...
    ) -> None: ...
