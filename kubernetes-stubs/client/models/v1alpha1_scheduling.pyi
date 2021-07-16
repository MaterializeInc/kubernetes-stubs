import datetime
import typing

import kubernetes.client

class V1alpha1Scheduling:
    node_selector: typing.Optional[dict[str, str]]
    tolerations: typing.Optional[list[kubernetes.client.V1Toleration]]
    def __init__(
        self,
        *,
        node_selector: typing.Optional[dict[str, str]] = ...,
        tolerations: typing.Optional[list[kubernetes.client.V1Toleration]] = ...
    ) -> None: ...
