import datetime
import typing

import kubernetes.client

class V1beta3NonResourcePolicyRule:
    non_resource_ur_ls: list[str]
    verbs: list[str]
    def __init__(self, *, non_resource_ur_ls: list[str], verbs: list[str]) -> None: ...
    def to_dict(self) -> V1beta3NonResourcePolicyRuleDict: ...

class V1beta3NonResourcePolicyRuleDict(typing.TypedDict, total=False):
    nonResourceURLs: list[str]
    verbs: list[str]
