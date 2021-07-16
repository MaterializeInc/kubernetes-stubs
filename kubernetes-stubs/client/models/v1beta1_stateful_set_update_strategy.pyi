import datetime
import typing

import kubernetes.client

class V1beta1StatefulSetUpdateStrategy:
    rolling_update: typing.Optional[
        kubernetes.client.V1beta1RollingUpdateStatefulSetStrategy
    ]
    type: typing.Optional[str]
    def __init__(
        self,
        *,
        rolling_update: typing.Optional[
            kubernetes.client.V1beta1RollingUpdateStatefulSetStrategy
        ] = ...,
        type: typing.Optional[str] = ...
    ) -> None: ...
