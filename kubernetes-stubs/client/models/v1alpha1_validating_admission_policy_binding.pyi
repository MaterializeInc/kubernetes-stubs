import datetime
import typing

import kubernetes.client

class V1alpha1ValidatingAdmissionPolicyBinding:
    api_version: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes.client.V1ObjectMeta]
    spec: typing.Optional[
        kubernetes.client.V1alpha1ValidatingAdmissionPolicyBindingSpec
    ]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes.client.V1ObjectMeta] = ...,
        spec: typing.Optional[
            kubernetes.client.V1alpha1ValidatingAdmissionPolicyBindingSpec
        ] = ...
    ) -> None: ...
    def to_dict(self) -> V1alpha1ValidatingAdmissionPolicyBindingDict: ...

class V1alpha1ValidatingAdmissionPolicyBindingDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes.client.V1ObjectMetaDict]
    spec: typing.Optional[
        kubernetes.client.V1alpha1ValidatingAdmissionPolicyBindingSpecDict
    ]
