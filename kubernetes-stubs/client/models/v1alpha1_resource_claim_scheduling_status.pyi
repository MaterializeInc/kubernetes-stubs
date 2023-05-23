import datetime
import typing

import kubernetes.client

class V1alpha1ResourceClaimSchedulingStatus:
    name: typing.Optional[str]
    unsuitable_nodes: typing.Optional[list[str]]
    def __init__(
        self,
        *,
        name: typing.Optional[str] = ...,
        unsuitable_nodes: typing.Optional[list[str]] = ...
    ) -> None: ...
    def to_dict(self) -> V1alpha1ResourceClaimSchedulingStatusDict: ...

class V1alpha1ResourceClaimSchedulingStatusDict(typing.TypedDict, total=False):
    name: typing.Optional[str]
    unsuitableNodes: typing.Optional[list[str]]
