import datetime
import typing

import kubernetes.client

class ExtensionsV1beta1DeploymentRollback:
    api_version: typing.Optional[str]
    kind: typing.Optional[str]
    name: str
    rollback_to: kubernetes.client.ExtensionsV1beta1RollbackConfig
    updated_annotations: typing.Optional[dict[str, str]]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        name: str,
        rollback_to: kubernetes.client.ExtensionsV1beta1RollbackConfig,
        updated_annotations: typing.Optional[dict[str, str]] = ...
    ) -> None: ...
