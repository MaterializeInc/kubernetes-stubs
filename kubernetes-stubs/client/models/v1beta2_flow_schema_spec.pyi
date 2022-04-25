import datetime
import typing

import kubernetes.client

class V1beta2FlowSchemaSpec:
    distinguisher_method: typing.Optional[
        kubernetes.client.V1beta2FlowDistinguisherMethod
    ]
    matching_precedence: typing.Optional[int]
    priority_level_configuration: kubernetes.client.V1beta2PriorityLevelConfigurationReference
    rules: typing.Optional[list[kubernetes.client.V1beta2PolicyRulesWithSubjects]]
    def __init__(
        self,
        *,
        distinguisher_method: typing.Optional[
            kubernetes.client.V1beta2FlowDistinguisherMethod
        ] = ...,
        matching_precedence: typing.Optional[int] = ...,
        priority_level_configuration: kubernetes.client.V1beta2PriorityLevelConfigurationReference,
        rules: typing.Optional[
            list[kubernetes.client.V1beta2PolicyRulesWithSubjects]
        ] = ...
    ) -> None: ...
    def to_dict(self) -> V1beta2FlowSchemaSpecDict: ...

class V1beta2FlowSchemaSpecDict(typing.TypedDict, total=False):
    distinguisherMethod: typing.Optional[
        kubernetes.client.V1beta2FlowDistinguisherMethodDict
    ]
    matchingPrecedence: typing.Optional[int]
    priorityLevelConfiguration: kubernetes.client.V1beta2PriorityLevelConfigurationReferenceDict
    rules: typing.Optional[list[kubernetes.client.V1beta2PolicyRulesWithSubjectsDict]]
