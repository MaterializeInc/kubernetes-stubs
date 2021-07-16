import datetime
import typing

import kubernetes.client

class V1NodeDaemonEndpoints:
    kubelet_endpoint: typing.Optional[kubernetes.client.V1DaemonEndpoint]
    def __init__(
        self,
        *,
        kubelet_endpoint: typing.Optional[kubernetes.client.V1DaemonEndpoint] = ...
    ) -> None: ...
