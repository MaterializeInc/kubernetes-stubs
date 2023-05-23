import datetime
import typing

import kubernetes.client

class V1alpha1AllocationResult:
    available_on_nodes: typing.Optional[kubernetes.client.V1NodeSelector]
    resource_handle: typing.Optional[str]
    shareable: typing.Optional[bool]
    def __init__(
        self,
        *,
        available_on_nodes: typing.Optional[kubernetes.client.V1NodeSelector] = ...,
        resource_handle: typing.Optional[str] = ...,
        shareable: typing.Optional[bool] = ...
    ) -> None: ...
    def to_dict(self) -> V1alpha1AllocationResultDict: ...

class V1alpha1AllocationResultDict(typing.TypedDict, total=False):
    availableOnNodes: typing.Optional[kubernetes.client.V1NodeSelectorDict]
    resourceHandle: typing.Optional[str]
    shareable: typing.Optional[bool]
