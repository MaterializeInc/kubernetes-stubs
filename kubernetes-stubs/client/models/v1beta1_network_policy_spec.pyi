import datetime
import typing

import kubernetes.client

class V1beta1NetworkPolicySpec:
    egress: typing.Optional[list[kubernetes.client.V1beta1NetworkPolicyEgressRule]]
    ingress: typing.Optional[list[kubernetes.client.V1beta1NetworkPolicyIngressRule]]
    pod_selector: kubernetes.client.V1LabelSelector
    policy_types: typing.Optional[list[str]]
    def __init__(
        self,
        *,
        egress: typing.Optional[
            list[kubernetes.client.V1beta1NetworkPolicyEgressRule]
        ] = ...,
        ingress: typing.Optional[
            list[kubernetes.client.V1beta1NetworkPolicyIngressRule]
        ] = ...,
        pod_selector: kubernetes.client.V1LabelSelector,
        policy_types: typing.Optional[list[str]] = ...
    ) -> None: ...
