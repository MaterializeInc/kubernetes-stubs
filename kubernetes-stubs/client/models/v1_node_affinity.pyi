import datetime
import typing

import kubernetes.client

class V1NodeAffinity:
    preferred_during_scheduling_ignored_during_execution: typing.Optional[
        list[kubernetes.client.V1PreferredSchedulingTerm]
    ]
    required_during_scheduling_ignored_during_execution: typing.Optional[
        kubernetes.client.V1NodeSelector
    ]
    def __init__(
        self,
        *,
        preferred_during_scheduling_ignored_during_execution: typing.Optional[
            list[kubernetes.client.V1PreferredSchedulingTerm]
        ] = ...,
        required_during_scheduling_ignored_during_execution: typing.Optional[
            kubernetes.client.V1NodeSelector
        ] = ...
    ) -> None: ...
