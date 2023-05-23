import datetime
import typing

import kubernetes.client

class V1alpha1ValidatingAdmissionPolicySpec:
    failure_policy: typing.Optional[str]
    match_constraints: typing.Optional[kubernetes.client.V1alpha1MatchResources]
    param_kind: typing.Optional[kubernetes.client.V1alpha1ParamKind]
    validations: list[kubernetes.client.V1alpha1Validation]
    def __init__(
        self,
        *,
        failure_policy: typing.Optional[str] = ...,
        match_constraints: typing.Optional[
            kubernetes.client.V1alpha1MatchResources
        ] = ...,
        param_kind: typing.Optional[kubernetes.client.V1alpha1ParamKind] = ...,
        validations: list[kubernetes.client.V1alpha1Validation]
    ) -> None: ...
    def to_dict(self) -> V1alpha1ValidatingAdmissionPolicySpecDict: ...

class V1alpha1ValidatingAdmissionPolicySpecDict(typing.TypedDict, total=False):
    failurePolicy: typing.Optional[str]
    matchConstraints: typing.Optional[kubernetes.client.V1alpha1MatchResourcesDict]
    paramKind: typing.Optional[kubernetes.client.V1alpha1ParamKindDict]
    validations: list[kubernetes.client.V1alpha1ValidationDict]
