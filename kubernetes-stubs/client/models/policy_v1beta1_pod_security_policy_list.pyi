import datetime
import typing

import kubernetes.client

class PolicyV1beta1PodSecurityPolicyList:
    api_version: typing.Optional[str]
    items: list[kubernetes.client.PolicyV1beta1PodSecurityPolicy]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes.client.V1ListMeta]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        items: list[kubernetes.client.PolicyV1beta1PodSecurityPolicy],
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes.client.V1ListMeta] = ...
    ) -> None: ...
