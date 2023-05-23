import datetime
import typing

import kubernetes.client

class V1alpha1ClusterCIDRSpec:
    ipv4: typing.Optional[str]
    ipv6: typing.Optional[str]
    node_selector: typing.Optional[kubernetes.client.V1NodeSelector]
    per_node_host_bits: int
    def __init__(
        self,
        *,
        ipv4: typing.Optional[str] = ...,
        ipv6: typing.Optional[str] = ...,
        node_selector: typing.Optional[kubernetes.client.V1NodeSelector] = ...,
        per_node_host_bits: int
    ) -> None: ...
    def to_dict(self) -> V1alpha1ClusterCIDRSpecDict: ...

class V1alpha1ClusterCIDRSpecDict(typing.TypedDict, total=False):
    ipv4: typing.Optional[str]
    ipv6: typing.Optional[str]
    nodeSelector: typing.Optional[kubernetes.client.V1NodeSelectorDict]
    perNodeHostBits: int
