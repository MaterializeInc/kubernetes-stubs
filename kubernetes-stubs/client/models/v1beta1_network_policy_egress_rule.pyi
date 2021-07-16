import datetime
import typing

import kubernetes.client

class V1beta1NetworkPolicyEgressRule:
    ports: typing.Optional[list[kubernetes.client.V1beta1NetworkPolicyPort]]
    to: typing.Optional[list[kubernetes.client.V1beta1NetworkPolicyPeer]]
    def __init__(
        self,
        *,
        ports: typing.Optional[list[kubernetes.client.V1beta1NetworkPolicyPort]] = ...,
        to: typing.Optional[list[kubernetes.client.V1beta1NetworkPolicyPeer]] = ...
    ) -> None: ...
