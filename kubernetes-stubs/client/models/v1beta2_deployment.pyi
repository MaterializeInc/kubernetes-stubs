import datetime
import typing

import kubernetes.client

class V1beta2Deployment:
    api_version: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes.client.V1ObjectMeta]
    spec: typing.Optional[kubernetes.client.V1beta2DeploymentSpec]
    status: typing.Optional[kubernetes.client.V1beta2DeploymentStatus]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes.client.V1ObjectMeta] = ...,
        spec: typing.Optional[kubernetes.client.V1beta2DeploymentSpec] = ...,
        status: typing.Optional[kubernetes.client.V1beta2DeploymentStatus] = ...
    ) -> None: ...
