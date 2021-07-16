import datetime
import typing

import kubernetes.client

class V1StatefulSetUpdateStrategy:
    rolling_update: typing.Optional[
        kubernetes.client.V1RollingUpdateStatefulSetStrategy
    ]
    type: typing.Optional[str]
    def __init__(
        self,
        *,
        rolling_update: typing.Optional[
            kubernetes.client.V1RollingUpdateStatefulSetStrategy
        ] = ...,
        type: typing.Optional[str] = ...
    ) -> None: ...
