import datetime
import typing

import kubernetes.client

class V1HTTPIngressRuleValue:
    paths: list[kubernetes.client.V1HTTPIngressPath]
    def __init__(self, *, paths: list[kubernetes.client.V1HTTPIngressPath]) -> None: ...
    def to_dict(self) -> V1HTTPIngressRuleValueDict: ...

class V1HTTPIngressRuleValueDict(typing.TypedDict, total=False):
    paths: list[kubernetes.client.V1HTTPIngressPathDict]
