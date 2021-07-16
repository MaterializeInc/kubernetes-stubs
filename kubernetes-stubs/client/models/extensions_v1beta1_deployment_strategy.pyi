import datetime
import typing

import kubernetes.client

class ExtensionsV1beta1DeploymentStrategy:
    rolling_update: typing.Optional[
        kubernetes.client.ExtensionsV1beta1RollingUpdateDeployment
    ]
    type: typing.Optional[str]
    def __init__(
        self,
        *,
        rolling_update: typing.Optional[
            kubernetes.client.ExtensionsV1beta1RollingUpdateDeployment
        ] = ...,
        type: typing.Optional[str] = ...
    ) -> None: ...
