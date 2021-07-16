import datetime
import typing

import kubernetes.client

class PolicyV1beta1PodSecurityPolicy:
    api_version: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes.client.V1ObjectMeta]
    spec: typing.Optional[kubernetes.client.PolicyV1beta1PodSecurityPolicySpec]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes.client.V1ObjectMeta] = ...,
        spec: typing.Optional[
            kubernetes.client.PolicyV1beta1PodSecurityPolicySpec
        ] = ...
    ) -> None: ...
