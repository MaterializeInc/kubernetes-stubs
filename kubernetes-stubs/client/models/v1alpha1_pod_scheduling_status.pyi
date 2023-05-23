import datetime
import typing

import kubernetes.client

class V1alpha1PodSchedulingStatus:
    resource_claims: typing.Optional[
        list[kubernetes.client.V1alpha1ResourceClaimSchedulingStatus]
    ]
    def __init__(
        self,
        *,
        resource_claims: typing.Optional[
            list[kubernetes.client.V1alpha1ResourceClaimSchedulingStatus]
        ] = ...
    ) -> None: ...
    def to_dict(self) -> V1alpha1PodSchedulingStatusDict: ...

class V1alpha1PodSchedulingStatusDict(typing.TypedDict, total=False):
    resourceClaims: typing.Optional[
        list[kubernetes.client.V1alpha1ResourceClaimSchedulingStatusDict]
    ]
