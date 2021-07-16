import datetime
import typing

import kubernetes.client

class V1NodeConfigSource:
    config_map: typing.Optional[kubernetes.client.V1ConfigMapNodeConfigSource]
    def __init__(
        self,
        *,
        config_map: typing.Optional[kubernetes.client.V1ConfigMapNodeConfigSource] = ...
    ) -> None: ...
