import datetime
import typing

import kubernetes.client

class V1alpha1ResourcePolicyRule:
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
