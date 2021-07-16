import datetime
import typing

import kubernetes.client

class V1alpha1FlowSchemaSpec:
    distinguisher_method: typing.Optional[
        kubernetes.client.V1alpha1FlowDistinguisherMethod
    ]
    matching_precedence: typing.Optional[int]
    priority_level_configuration: kubernetes.client.V1alpha1PriorityLevelConfigurationReference
    rules: typing.Optional[list[kubernetes.client.V1alpha1PolicyRulesWithSubjects]]
    def __init__(
        self,
        *,
        distinguisher_method: typing.Optional[
            kubernetes.client.V1alpha1FlowDistinguisherMethod
        ] = ...,
        matching_precedence: typing.Optional[int] = ...,
        priority_level_configuration: kubernetes.client.V1alpha1PriorityLevelConfigurationReference,
        rules: typing.Optional[
            list[kubernetes.client.V1alpha1PolicyRulesWithSubjects]
        ] = ...
    ) -> None: ...
