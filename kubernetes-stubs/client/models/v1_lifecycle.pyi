import datetime
import typing

import kubernetes.client

class V1Lifecycle:
    post_start: typing.Optional[kubernetes.client.V1Handler]
    pre_stop: typing.Optional[kubernetes.client.V1Handler]
    def __init__(
        self,
        *,
        post_start: typing.Optional[kubernetes.client.V1Handler] = ...,
        pre_stop: typing.Optional[kubernetes.client.V1Handler] = ...
    ) -> None: ...
