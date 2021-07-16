import datetime
import typing

import kubernetes.client

class V1ContainerState:
    running: typing.Optional[kubernetes.client.V1ContainerStateRunning]
    terminated: typing.Optional[kubernetes.client.V1ContainerStateTerminated]
    waiting: typing.Optional[kubernetes.client.V1ContainerStateWaiting]
    def __init__(
        self,
        *,
        running: typing.Optional[kubernetes.client.V1ContainerStateRunning] = ...,
        terminated: typing.Optional[kubernetes.client.V1ContainerStateTerminated] = ...,
        waiting: typing.Optional[kubernetes.client.V1ContainerStateWaiting] = ...
    ) -> None: ...
