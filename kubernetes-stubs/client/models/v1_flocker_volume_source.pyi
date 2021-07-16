import datetime
import typing

import kubernetes.client

class V1FlockerVolumeSource:
    dataset_name: typing.Optional[str]
    dataset_uuid: typing.Optional[str]
    def __init__(
        self,
        *,
        dataset_name: typing.Optional[str] = ...,
        dataset_uuid: typing.Optional[str] = ...
    ) -> None: ...
