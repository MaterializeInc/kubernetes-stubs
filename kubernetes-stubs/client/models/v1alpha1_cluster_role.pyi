import datetime
import typing

import kubernetes.client

class V1alpha1ClusterRole:
    aggregation_rule: typing.Optional[kubernetes.client.V1alpha1AggregationRule]
    api_version: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes.client.V1ObjectMeta]
    rules: typing.Optional[list[kubernetes.client.V1alpha1PolicyRule]]
    def __init__(
        self,
        *,
        aggregation_rule: typing.Optional[
            kubernetes.client.V1alpha1AggregationRule
        ] = ...,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes.client.V1ObjectMeta] = ...,
        rules: typing.Optional[list[kubernetes.client.V1alpha1PolicyRule]] = ...
    ) -> None: ...
