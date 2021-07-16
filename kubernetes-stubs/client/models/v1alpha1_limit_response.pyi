import datetime
import typing

import kubernetes.client

class V1alpha1LimitResponse:
    queuing: typing.Optional[kubernetes.client.V1alpha1QueuingConfiguration]
    type: str
    def __init__(
        self,
        *,
        queuing: typing.Optional[kubernetes.client.V1alpha1QueuingConfiguration] = ...,
        type: str
    ) -> None: ...
