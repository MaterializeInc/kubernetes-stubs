import datetime
import typing

import kubernetes.client

class V1APIServiceSpec:
    ca_bundle: typing.Optional[str]
    group: typing.Optional[str]
    group_priority_minimum: int
    insecure_skip_tls_verify: typing.Optional[bool]
    service: kubernetes.client.ApiregistrationV1ServiceReference
    version: typing.Optional[str]
    version_priority: int
    def __init__(
        self,
        *,
        ca_bundle: typing.Optional[str] = ...,
        group: typing.Optional[str] = ...,
        group_priority_minimum: int,
        insecure_skip_tls_verify: typing.Optional[bool] = ...,
        service: kubernetes.client.ApiregistrationV1ServiceReference,
        version: typing.Optional[str] = ...,
        version_priority: int
    ) -> None: ...
