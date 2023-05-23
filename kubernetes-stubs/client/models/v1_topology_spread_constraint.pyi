import datetime
import typing

import kubernetes.client

class V1TopologySpreadConstraint:
    label_selector: typing.Optional[kubernetes.client.V1LabelSelector]
    match_label_keys: typing.Optional[list[str]]
    max_skew: int
    min_domains: typing.Optional[int]
    node_affinity_policy: typing.Optional[str]
    node_taints_policy: typing.Optional[str]
    topology_key: str
    when_unsatisfiable: str
    def __init__(
        self,
        *,
        label_selector: typing.Optional[kubernetes.client.V1LabelSelector] = ...,
        match_label_keys: typing.Optional[list[str]] = ...,
        max_skew: int,
        min_domains: typing.Optional[int] = ...,
        node_affinity_policy: typing.Optional[str] = ...,
        node_taints_policy: typing.Optional[str] = ...,
        topology_key: str,
        when_unsatisfiable: str
    ) -> None: ...
    def to_dict(self) -> V1TopologySpreadConstraintDict: ...

class V1TopologySpreadConstraintDict(typing.TypedDict, total=False):
    labelSelector: typing.Optional[kubernetes.client.V1LabelSelectorDict]
    matchLabelKeys: typing.Optional[list[str]]
    maxSkew: int
    minDomains: typing.Optional[int]
    nodeAffinityPolicy: typing.Optional[str]
    nodeTaintsPolicy: typing.Optional[str]
    topologyKey: str
    whenUnsatisfiable: str
