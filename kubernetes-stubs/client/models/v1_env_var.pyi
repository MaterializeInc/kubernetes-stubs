import datetime
import typing

import kubernetes.client

class V1EnvVar:
    name: str
    value: typing.Optional[str]
    value_from: typing.Optional[kubernetes.client.V1EnvVarSource]
    def __init__(
        self,
        *,
        name: str,
        value: typing.Optional[str] = ...,
        value_from: typing.Optional[kubernetes.client.V1EnvVarSource] = ...
    ) -> None: ...
