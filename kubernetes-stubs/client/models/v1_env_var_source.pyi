import datetime
import typing

import kubernetes.client

class V1EnvVarSource:
    config_map_key_ref: typing.Optional[kubernetes.client.V1ConfigMapKeySelector]
    field_ref: typing.Optional[kubernetes.client.V1ObjectFieldSelector]
    resource_field_ref: typing.Optional[kubernetes.client.V1ResourceFieldSelector]
    secret_key_ref: typing.Optional[kubernetes.client.V1SecretKeySelector]
    def __init__(
        self,
        *,
        config_map_key_ref: typing.Optional[
            kubernetes.client.V1ConfigMapKeySelector
        ] = ...,
        field_ref: typing.Optional[kubernetes.client.V1ObjectFieldSelector] = ...,
        resource_field_ref: typing.Optional[
            kubernetes.client.V1ResourceFieldSelector
        ] = ...,
        secret_key_ref: typing.Optional[kubernetes.client.V1SecretKeySelector] = ...
    ) -> None: ...
