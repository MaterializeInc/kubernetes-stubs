import datetime
import typing

import kubernetes.client

class V1CustomResourceDefinitionStatus:
    accepted_names: kubernetes.client.V1CustomResourceDefinitionNames
    conditions: typing.Optional[
        list[kubernetes.client.V1CustomResourceDefinitionCondition]
    ]
    stored_versions: list[str]
    def __init__(
        self,
        *,
        accepted_names: kubernetes.client.V1CustomResourceDefinitionNames,
        conditions: typing.Optional[
            list[kubernetes.client.V1CustomResourceDefinitionCondition]
        ] = ...,
        stored_versions: list[str]
    ) -> None: ...
