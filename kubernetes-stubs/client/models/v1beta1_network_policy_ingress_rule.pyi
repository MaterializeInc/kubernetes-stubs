import datetime
import typing

import kubernetes.client

class V1beta1NetworkPolicyIngressRule:
    from: typing.Optional[list[kubernetes.client.V1beta1NetworkPolicyPeer]]
    ports: typing.Optional[list[kubernetes.client.V1beta1NetworkPolicyPort]]
    
    def __init__(self, *, from: typing.Optional[list[kubernetes.client.V1beta1NetworkPolicyPeer]] = ..., ports: typing.Optional[list[kubernetes.client.V1beta1NetworkPolicyPort]] = ...) -> None:
        ...
