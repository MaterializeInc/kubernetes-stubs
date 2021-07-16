import datetime
import typing

import kubernetes.client

class V1FlexPersistentVolumeSource:
    driver: str
    fs_type: typing.Optional[str]
    options: typing.Optional[dict[str, str]]
    read_only: typing.Optional[bool]
    secret_ref: typing.Optional[kubernetes.client.V1SecretReference]
    def __init__(
        self,
        *,
        driver: str,
        fs_type: typing.Optional[str] = ...,
        options: typing.Optional[dict[str, str]] = ...,
        read_only: typing.Optional[bool] = ...,
        secret_ref: typing.Optional[kubernetes.client.V1SecretReference] = ...
    ) -> None: ...
