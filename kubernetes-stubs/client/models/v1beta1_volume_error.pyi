import datetime
import typing

import kubernetes.client

class V1beta1VolumeError:
    message: typing.Optional[str]
    time: typing.Optional[datetime.datetime]
    def __init__(
        self,
        *,
        message: typing.Optional[str] = ...,
        time: typing.Optional[datetime.datetime] = ...
    ) -> None: ...
