import datetime
import typing

import kubernetes.client

class V1CSIPersistentVolumeSource:
    controller_expand_secret_ref: typing.Optional[kubernetes.client.V1SecretReference]
    controller_publish_secret_ref: typing.Optional[kubernetes.client.V1SecretReference]
    driver: str
    fs_type: typing.Optional[str]
    node_publish_secret_ref: typing.Optional[kubernetes.client.V1SecretReference]
    node_stage_secret_ref: typing.Optional[kubernetes.client.V1SecretReference]
    read_only: typing.Optional[bool]
    volume_attributes: typing.Optional[dict[str, str]]
    volume_handle: str
    def __init__(
        self,
        *,
        controller_expand_secret_ref: typing.Optional[
            kubernetes.client.V1SecretReference
        ] = ...,
        controller_publish_secret_ref: typing.Optional[
            kubernetes.client.V1SecretReference
        ] = ...,
        driver: str,
        fs_type: typing.Optional[str] = ...,
        node_publish_secret_ref: typing.Optional[
            kubernetes.client.V1SecretReference
        ] = ...,
        node_stage_secret_ref: typing.Optional[
            kubernetes.client.V1SecretReference
        ] = ...,
        read_only: typing.Optional[bool] = ...,
        volume_attributes: typing.Optional[dict[str, str]] = ...,
        volume_handle: str
    ) -> None: ...
