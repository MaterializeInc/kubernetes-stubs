import datetime
import typing

import kubernetes.client

class V1CustomResourceDefinitionStatus:
    accepted_names: typing.Optional[kubernetes.client.V1CustomResourceDefinitionNames]
    conditions: typing.Optional[
        list[kubernetes.client.V1CustomResourceDefinitionCondition]
    ]
    stored_versions: typing.Optional[list[str]]
    def __init__(
        self,
        *,
        accepted_names: typing.Optional[
            kubernetes.client.V1CustomResourceDefinitionNames
        ] = ...,
        conditions: typing.Optional[
            list[kubernetes.client.V1CustomResourceDefinitionCondition]
        ] = ...,
        stored_versions: typing.Optional[list[str]] = ...
    ) -> None: ...
