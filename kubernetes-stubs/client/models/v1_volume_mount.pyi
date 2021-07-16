import datetime
import typing

import kubernetes.client

class V1VolumeMount:
    mount_path: str
    mount_propagation: typing.Optional[str]
    name: str
    read_only: typing.Optional[bool]
    sub_path: typing.Optional[str]
    sub_path_expr: typing.Optional[str]
    def __init__(
        self,
        *,
        mount_path: str,
        mount_propagation: typing.Optional[str] = ...,
        name: str,
        read_only: typing.Optional[bool] = ...,
        sub_path: typing.Optional[str] = ...,
        sub_path_expr: typing.Optional[str] = ...
    ) -> None: ...
