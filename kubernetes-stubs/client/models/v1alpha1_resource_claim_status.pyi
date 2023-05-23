import datetime
import typing

import kubernetes.client

class V1alpha1ResourceClaimStatus:
    allocation: typing.Optional[kubernetes.client.V1alpha1AllocationResult]
    deallocation_requested: typing.Optional[bool]
    driver_name: typing.Optional[str]
    reserved_for: typing.Optional[
        list[kubernetes.client.V1alpha1ResourceClaimConsumerReference]
    ]
    def __init__(
        self,
        *,
        allocation: typing.Optional[kubernetes.client.V1alpha1AllocationResult] = ...,
        deallocation_requested: typing.Optional[bool] = ...,
        driver_name: typing.Optional[str] = ...,
        reserved_for: typing.Optional[
            list[kubernetes.client.V1alpha1ResourceClaimConsumerReference]
        ] = ...
    ) -> None: ...
    def to_dict(self) -> V1alpha1ResourceClaimStatusDict: ...

class V1alpha1ResourceClaimStatusDict(typing.TypedDict, total=False):
    allocation: typing.Optional[kubernetes.client.V1alpha1AllocationResultDict]
    deallocationRequested: typing.Optional[bool]
    driverName: typing.Optional[str]
    reservedFor: typing.Optional[
        list[kubernetes.client.V1alpha1ResourceClaimConsumerReferenceDict]
    ]
