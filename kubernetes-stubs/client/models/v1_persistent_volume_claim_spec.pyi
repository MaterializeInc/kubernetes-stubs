import datetime
import typing

import kubernetes.client

class V1PersistentVolumeClaimSpec:
    access_modes: typing.Optional[list[str]]
    data_source: typing.Optional[kubernetes.client.V1TypedLocalObjectReference]
    resources: typing.Optional[kubernetes.client.V1ResourceRequirements]
    selector: typing.Optional[kubernetes.client.V1LabelSelector]
    storage_class_name: typing.Optional[str]
    volume_mode: typing.Optional[str]
    volume_name: typing.Optional[str]
    def __init__(
        self,
        *,
        access_modes: typing.Optional[list[str]] = ...,
        data_source: typing.Optional[
            kubernetes.client.V1TypedLocalObjectReference
        ] = ...,
        resources: typing.Optional[kubernetes.client.V1ResourceRequirements] = ...,
        selector: typing.Optional[kubernetes.client.V1LabelSelector] = ...,
        storage_class_name: typing.Optional[str] = ...,
        volume_mode: typing.Optional[str] = ...,
        volume_name: typing.Optional[str] = ...
    ) -> None: ...
