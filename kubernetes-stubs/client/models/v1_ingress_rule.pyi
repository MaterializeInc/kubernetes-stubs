import datetime
import typing

import kubernetes.client

class V1IngressRule:
    host: typing.Optional[str]
    http: typing.Optional[kubernetes.client.V1HTTPIngressRuleValue]
    def __init__(
        self,
        *,
        host: typing.Optional[str] = ...,
        http: typing.Optional[kubernetes.client.V1HTTPIngressRuleValue] = ...
    ) -> None: ...
    def to_dict(self) -> V1IngressRuleDict: ...

class V1IngressRuleDict(typing.TypedDict, total=False):
    host: typing.Optional[str]
    http: typing.Optional[kubernetes.client.V1HTTPIngressRuleValueDict]
