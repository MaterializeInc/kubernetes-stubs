import datetime
import typing

import kubernetes.client

class V1GlusterfsPersistentVolumeSource:
    endpoints: str
    endpoints_namespace: typing.Optional[str]
    path: str
    read_only: typing.Optional[bool]
    def __init__(
        self,
        *,
        endpoints: str,
        endpoints_namespace: typing.Optional[str] = ...,
        path: str,
        read_only: typing.Optional[bool] = ...
    ) -> None: ...
