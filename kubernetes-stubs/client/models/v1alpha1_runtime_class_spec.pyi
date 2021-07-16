import datetime
import typing

import kubernetes.client

class V1alpha1RuntimeClassSpec:
    overhead: typing.Optional[kubernetes.client.V1alpha1Overhead]
    runtime_handler: str
    scheduling: typing.Optional[kubernetes.client.V1alpha1Scheduling]
    def __init__(
        self,
        *,
        overhead: typing.Optional[kubernetes.client.V1alpha1Overhead] = ...,
        runtime_handler: str,
        scheduling: typing.Optional[kubernetes.client.V1alpha1Scheduling] = ...
    ) -> None: ...
