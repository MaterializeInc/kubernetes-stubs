import datetime
import typing

import kubernetes.client

class V1ResourceRequirements:
    claims: typing.Optional[list[kubernetes.client.V1ResourceClaim]]
    limits: typing.Optional[dict[str, str]]
    requests: typing.Optional[dict[str, str]]
    def __init__(
        self,
        *,
        claims: typing.Optional[list[kubernetes.client.V1ResourceClaim]] = ...,
        limits: typing.Optional[dict[str, str]] = ...,
        requests: typing.Optional[dict[str, str]] = ...
    ) -> None: ...
    def to_dict(self) -> V1ResourceRequirementsDict: ...

class V1ResourceRequirementsDict(typing.TypedDict, total=False):
    claims: typing.Optional[list[kubernetes.client.V1ResourceClaimDict]]
    limits: typing.Optional[dict[str, str]]
    requests: typing.Optional[dict[str, str]]
