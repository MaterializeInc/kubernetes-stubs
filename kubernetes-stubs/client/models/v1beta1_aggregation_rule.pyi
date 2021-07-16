import datetime
import typing

import kubernetes.client

class V1beta1AggregationRule:
    cluster_role_selectors: typing.Optional[list[kubernetes.client.V1LabelSelector]]
    def __init__(
        self,
        *,
        cluster_role_selectors: typing.Optional[
            list[kubernetes.client.V1LabelSelector]
        ] = ...
    ) -> None: ...
