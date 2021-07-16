import datetime
import typing

import kubernetes.client

class V1TopologySpreadConstraint:
    label_selector: typing.Optional[kubernetes.client.V1LabelSelector]
    max_skew: int
    topology_key: str
    when_unsatisfiable: str
    def __init__(
        self,
        *,
        label_selector: typing.Optional[kubernetes.client.V1LabelSelector] = ...,
        max_skew: int,
        topology_key: str,
        when_unsatisfiable: str
    ) -> None: ...
