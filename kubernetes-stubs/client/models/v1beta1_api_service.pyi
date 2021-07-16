import datetime
import typing

import kubernetes.client

class V1beta1APIService:
    api_version: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes.client.V1ObjectMeta]
    spec: typing.Optional[kubernetes.client.V1beta1APIServiceSpec]
    status: typing.Optional[kubernetes.client.V1beta1APIServiceStatus]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes.client.V1ObjectMeta] = ...,
        spec: typing.Optional[kubernetes.client.V1beta1APIServiceSpec] = ...,
        status: typing.Optional[kubernetes.client.V1beta1APIServiceStatus] = ...
    ) -> None: ...
