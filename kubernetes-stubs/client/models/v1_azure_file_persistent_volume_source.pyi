import datetime
import typing

import kubernetes.client

class V1AzureFilePersistentVolumeSource:
    read_only: typing.Optional[bool]
    secret_name: str
    secret_namespace: typing.Optional[str]
    share_name: str
    def __init__(
        self,
        *,
        read_only: typing.Optional[bool] = ...,
        secret_name: str,
        secret_namespace: typing.Optional[str] = ...,
        share_name: str
    ) -> None: ...
