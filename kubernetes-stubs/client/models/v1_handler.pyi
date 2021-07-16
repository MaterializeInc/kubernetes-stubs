import datetime
import typing

import kubernetes.client

class V1Handler:
    exec: typing.Optional[kubernetes.client.V1ExecAction]
    http_get: typing.Optional[kubernetes.client.V1HTTPGetAction]
    tcp_socket: typing.Optional[kubernetes.client.V1TCPSocketAction]
    def __init__(
        self,
        *,
        exec: typing.Optional[kubernetes.client.V1ExecAction] = ...,
        http_get: typing.Optional[kubernetes.client.V1HTTPGetAction] = ...,
        tcp_socket: typing.Optional[kubernetes.client.V1TCPSocketAction] = ...
    ) -> None: ...
