import datetime
import typing

import kubernetes.client

class NetworkingV1beta1HTTPIngressRuleValue:
    paths: list[kubernetes.client.NetworkingV1beta1HTTPIngressPath]
    def __init__(
        self, *, paths: list[kubernetes.client.NetworkingV1beta1HTTPIngressPath]
    ) -> None: ...
