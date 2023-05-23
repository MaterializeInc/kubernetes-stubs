import datetime
import typing

import kubernetes.client

class V1PodFailurePolicyOnExitCodesRequirement:
    container_name: typing.Optional[str]
    operator: str
    values: list[int]
    def __init__(
        self,
        *,
        container_name: typing.Optional[str] = ...,
        operator: str,
        values: list[int]
    ) -> None: ...
    def to_dict(self) -> V1PodFailurePolicyOnExitCodesRequirementDict: ...

class V1PodFailurePolicyOnExitCodesRequirementDict(typing.TypedDict, total=False):
    containerName: typing.Optional[str]
    operator: str
    values: list[int]
