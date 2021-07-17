import datetime
import typing

import kubernetes.client

class V1NetworkPolicyIngressRule:
    _from: typing.Optional[list[kubernetes.client.V1NetworkPolicyPeer]]
    ports: typing.Optional[list[kubernetes.client.V1NetworkPolicyPort]]
    def __init__(
        self,
        *,
        _from: typing.Optional[list[kubernetes.client.V1NetworkPolicyPeer]] = ...,
        ports: typing.Optional[list[kubernetes.client.V1NetworkPolicyPort]] = ...
    ) -> None: ...
