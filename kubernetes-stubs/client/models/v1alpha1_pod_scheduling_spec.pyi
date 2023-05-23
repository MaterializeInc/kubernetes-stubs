import datetime
import typing

import kubernetes.client

class V1alpha1PodSchedulingSpec:
    potential_nodes: typing.Optional[list[str]]
    selected_node: typing.Optional[str]
    def __init__(
        self,
        *,
        potential_nodes: typing.Optional[list[str]] = ...,
        selected_node: typing.Optional[str] = ...
    ) -> None: ...
    def to_dict(self) -> V1alpha1PodSchedulingSpecDict: ...

class V1alpha1PodSchedulingSpecDict(typing.TypedDict, total=False):
    potentialNodes: typing.Optional[list[str]]
    selectedNode: typing.Optional[str]
