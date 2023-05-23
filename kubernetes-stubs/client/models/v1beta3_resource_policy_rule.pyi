import datetime
import typing

import kubernetes.client

class V1beta3ResourcePolicyRule:
    api_groups: list[str]
    cluster_scope: typing.Optional[bool]
    namespaces: typing.Optional[list[str]]
    resources: list[str]
    verbs: list[str]
    def __init__(
        self,
        *,
        api_groups: list[str],
        cluster_scope: typing.Optional[bool] = ...,
        namespaces: typing.Optional[list[str]] = ...,
        resources: list[str],
        verbs: list[str]
    ) -> None: ...
    def to_dict(self) -> V1beta3ResourcePolicyRuleDict: ...

class V1beta3ResourcePolicyRuleDict(typing.TypedDict, total=False):
    apiGroups: list[str]
    clusterScope: typing.Optional[bool]
    namespaces: typing.Optional[list[str]]
    resources: list[str]
    verbs: list[str]
