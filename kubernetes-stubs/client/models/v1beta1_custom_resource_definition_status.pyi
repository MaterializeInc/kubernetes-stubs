import datetime
import typing

import kubernetes.client

class V1beta1CustomResourceDefinitionStatus:
    accepted_names: kubernetes.client.V1beta1CustomResourceDefinitionNames
    conditions: typing.Optional[
        list[kubernetes.client.V1beta1CustomResourceDefinitionCondition]
    ]
    stored_versions: list[str]
    def __init__(
        self,
        *,
        accepted_names: kubernetes.client.V1beta1CustomResourceDefinitionNames,
        conditions: typing.Optional[
            list[kubernetes.client.V1beta1CustomResourceDefinitionCondition]
        ] = ...,
        stored_versions: list[str]
    ) -> None: ...
