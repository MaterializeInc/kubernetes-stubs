import datetime
import typing

import kubernetes.client

class ExtensionsV1beta1AllowedHostPath:
    path_prefix: typing.Optional[str]
    read_only: typing.Optional[bool]
    def __init__(
        self,
        *,
        path_prefix: typing.Optional[str] = ...,
        read_only: typing.Optional[bool] = ...
    ) -> None: ...
