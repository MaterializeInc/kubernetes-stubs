import datetime
import typing

import kubernetes.client

class V1alpha1ValidatingAdmissionPolicyBindingSpec:
    match_resources: typing.Optional[kubernetes.client.V1alpha1MatchResources]
    param_ref: typing.Optional[kubernetes.client.V1alpha1ParamRef]
    policy_name: typing.Optional[str]
    def __init__(
        self,
        *,
        match_resources: typing.Optional[
            kubernetes.client.V1alpha1MatchResources
        ] = ...,
        param_ref: typing.Optional[kubernetes.client.V1alpha1ParamRef] = ...,
        policy_name: typing.Optional[str] = ...
    ) -> None: ...
    def to_dict(self) -> V1alpha1ValidatingAdmissionPolicyBindingSpecDict: ...

class V1alpha1ValidatingAdmissionPolicyBindingSpecDict(typing.TypedDict, total=False):
    matchResources: typing.Optional[kubernetes.client.V1alpha1MatchResourcesDict]
    paramRef: typing.Optional[kubernetes.client.V1alpha1ParamRefDict]
    policyName: typing.Optional[str]
