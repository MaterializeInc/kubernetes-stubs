import datetime
import typing

import kubernetes.client

class V1PodAffinity:
    preferred_during_scheduling_ignored_during_execution: typing.Optional[
        list[kubernetes.client.V1WeightedPodAffinityTerm]
    ]
    required_during_scheduling_ignored_during_execution: typing.Optional[
        list[kubernetes.client.V1PodAffinityTerm]
    ]
    def __init__(
        self,
        *,
        preferred_during_scheduling_ignored_during_execution: typing.Optional[
            list[kubernetes.client.V1WeightedPodAffinityTerm]
        ] = ...,
        required_during_scheduling_ignored_during_execution: typing.Optional[
            list[kubernetes.client.V1PodAffinityTerm]
        ] = ...
    ) -> None: ...
