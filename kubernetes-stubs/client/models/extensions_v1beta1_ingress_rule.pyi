import datetime
import typing

import kubernetes.client

class ExtensionsV1beta1IngressRule:
    host: typing.Optional[str]
    http: typing.Optional[kubernetes.client.ExtensionsV1beta1HTTPIngressRuleValue]
    def __init__(
        self,
        *,
        host: typing.Optional[str] = ...,
        http: typing.Optional[
            kubernetes.client.ExtensionsV1beta1HTTPIngressRuleValue
        ] = ...
    ) -> None: ...
