import datetime
import typing

import kubernetes.client

class V1JobStatus:
    active: typing.Optional[int]
    completed_indexes: typing.Optional[str]
    completion_time: typing.Optional[datetime.datetime]
    conditions: typing.Optional[list[kubernetes.client.V1JobCondition]]
    failed: typing.Optional[int]
    start_time: typing.Optional[datetime.datetime]
    succeeded: typing.Optional[int]
    uncounted_terminated_pods: typing.Optional[
        kubernetes.client.V1UncountedTerminatedPods
    ]

    def __init__(
        self,
        *,
        active: typing.Optional[int] = ...,
        completed_indexes: typing.Optional[str] = ...,
        completion_time: typing.Optional[datetime.datetime] = ...,
        conditions: typing.Optional[list[kubernetes.client.V1JobCondition]] = ...,
        failed: typing.Optional[int] = ...,
        start_time: typing.Optional[datetime.datetime] = ...,
        succeeded: typing.Optional[int] = ...,
        uncounted_terminated_pods: typing.Optional[
            kubernetes.client.V1UncountedTerminatedPods
        ] = ...
    ) -> None: ...
    def to_dict(self) -> V1JobStatusDict: ...

class V1JobStatusDict(typing.TypedDict, total=False):
    active: typing.Optional[int]
    completedIndexes: typing.Optional[str]
    completionTime: typing.Optional[datetime.datetime]
    conditions: typing.Optional[list[kubernetes.client.V1JobConditionDict]]
    failed: typing.Optional[int]
    startTime: typing.Optional[datetime.datetime]
    succeeded: typing.Optional[int]
    uncountedTerminatedPods: typing.Optional[
        kubernetes.client.V1UncountedTerminatedPodsDict
    ]
