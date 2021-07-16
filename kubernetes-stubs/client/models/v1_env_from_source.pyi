import datetime
import typing

import kubernetes.client

class V1EnvFromSource:
    config_map_ref: typing.Optional[kubernetes.client.V1ConfigMapEnvSource]
    prefix: typing.Optional[str]
    secret_ref: typing.Optional[kubernetes.client.V1SecretEnvSource]
    def __init__(
        self,
        *,
        config_map_ref: typing.Optional[kubernetes.client.V1ConfigMapEnvSource] = ...,
        prefix: typing.Optional[str] = ...,
        secret_ref: typing.Optional[kubernetes.client.V1SecretEnvSource] = ...
    ) -> None: ...
