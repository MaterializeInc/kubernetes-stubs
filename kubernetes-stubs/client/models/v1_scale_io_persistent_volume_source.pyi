import datetime
import typing

import kubernetes.client

class V1ScaleIOPersistentVolumeSource:
    fs_type: typing.Optional[str]
    gateway: str
    protection_domain: typing.Optional[str]
    read_only: typing.Optional[bool]
    secret_ref: kubernetes.client.V1SecretReference
    ssl_enabled: typing.Optional[bool]
    storage_mode: typing.Optional[str]
    storage_pool: typing.Optional[str]
    system: str
    volume_name: typing.Optional[str]
    def __init__(
        self,
        *,
        fs_type: typing.Optional[str] = ...,
        gateway: str,
        protection_domain: typing.Optional[str] = ...,
        read_only: typing.Optional[bool] = ...,
        secret_ref: kubernetes.client.V1SecretReference,
        ssl_enabled: typing.Optional[bool] = ...,
        storage_mode: typing.Optional[str] = ...,
        storage_pool: typing.Optional[str] = ...,
        system: str,
        volume_name: typing.Optional[str] = ...
    ) -> None: ...
