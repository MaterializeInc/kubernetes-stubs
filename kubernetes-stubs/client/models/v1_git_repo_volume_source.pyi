import datetime
import typing

import kubernetes.client

class V1GitRepoVolumeSource:
    directory: typing.Optional[str]
    repository: str
    revision: typing.Optional[str]
    def __init__(
        self,
        *,
        directory: typing.Optional[str] = ...,
        repository: str,
        revision: typing.Optional[str] = ...
    ) -> None: ...
