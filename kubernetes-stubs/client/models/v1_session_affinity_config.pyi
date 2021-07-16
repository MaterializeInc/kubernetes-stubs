import datetime
import typing

import kubernetes.client

class V1SessionAffinityConfig:
    client_ip: typing.Optional[kubernetes.client.V1ClientIPConfig]
    def __init__(
        self, *, client_ip: typing.Optional[kubernetes.client.V1ClientIPConfig] = ...
    ) -> None: ...
