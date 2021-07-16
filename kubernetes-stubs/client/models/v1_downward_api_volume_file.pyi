import datetime
import typing

import kubernetes.client

class V1DownwardAPIVolumeFile:
    field_ref: typing.Optional[kubernetes.client.V1ObjectFieldSelector]
    mode: typing.Optional[int]
    path: str
    resource_field_ref: typing.Optional[kubernetes.client.V1ResourceFieldSelector]
    def __init__(
        self,
        *,
        field_ref: typing.Optional[kubernetes.client.V1ObjectFieldSelector] = ...,
        mode: typing.Optional[int] = ...,
        path: str,
        resource_field_ref: typing.Optional[
            kubernetes.client.V1ResourceFieldSelector
        ] = ...
    ) -> None: ...
