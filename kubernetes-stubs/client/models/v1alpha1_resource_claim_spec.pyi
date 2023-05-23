import datetime
import typing

import kubernetes.client

class V1alpha1ResourceClaimSpec:
    allocation_mode: typing.Optional[str]
    parameters_ref: typing.Optional[
        kubernetes.client.V1alpha1ResourceClaimParametersReference
    ]
    resource_class_name: str
    def __init__(
        self,
        *,
        allocation_mode: typing.Optional[str] = ...,
        parameters_ref: typing.Optional[
            kubernetes.client.V1alpha1ResourceClaimParametersReference
        ] = ...,
        resource_class_name: str
    ) -> None: ...
    def to_dict(self) -> V1alpha1ResourceClaimSpecDict: ...

class V1alpha1ResourceClaimSpecDict(typing.TypedDict, total=False):
    allocationMode: typing.Optional[str]
    parametersRef: typing.Optional[
        kubernetes.client.V1alpha1ResourceClaimParametersReferenceDict
    ]
    resourceClassName: str
