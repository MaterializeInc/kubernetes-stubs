import datetime
import typing

import kubernetes.client

class V1VolumeProjection:
    config_map: typing.Optional[kubernetes.client.V1ConfigMapProjection]
    downward_api: typing.Optional[kubernetes.client.V1DownwardAPIProjection]
    secret: typing.Optional[kubernetes.client.V1SecretProjection]
    service_account_token: typing.Optional[
        kubernetes.client.V1ServiceAccountTokenProjection
    ]
    def __init__(
        self,
        *,
        config_map: typing.Optional[kubernetes.client.V1ConfigMapProjection] = ...,
        downward_api: typing.Optional[kubernetes.client.V1DownwardAPIProjection] = ...,
        secret: typing.Optional[kubernetes.client.V1SecretProjection] = ...,
        service_account_token: typing.Optional[
            kubernetes.client.V1ServiceAccountTokenProjection
        ] = ...
    ) -> None: ...
