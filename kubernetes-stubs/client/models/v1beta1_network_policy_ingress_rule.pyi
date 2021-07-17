import datetime
import typing

import kubernetes.client

class V1beta1NetworkPolicyIngressRule:
    _from: typing.Optional[list[kubernetes.client.V1beta1NetworkPolicyPeer]]
    ports: typing.Optional[list[kubernetes.client.V1beta1NetworkPolicyPort]]
    def __init__(
        self,
        *,
        _from: typing.Optional[list[kubernetes.client.V1beta1NetworkPolicyPeer]] = ...,
        ports: typing.Optional[list[kubernetes.client.V1beta1NetworkPolicyPort]] = ...
    ) -> None: ...
