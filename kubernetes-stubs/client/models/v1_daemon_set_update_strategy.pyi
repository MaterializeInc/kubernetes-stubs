import datetime
import typing

import kubernetes.client

class V1DaemonSetUpdateStrategy:
    rolling_update: typing.Optional[kubernetes.client.V1RollingUpdateDaemonSet]
    type: typing.Optional[str]
    def __init__(
        self,
        *,
        rolling_update: typing.Optional[
            kubernetes.client.V1RollingUpdateDaemonSet
        ] = ...,
        type: typing.Optional[str] = ...
    ) -> None: ...
