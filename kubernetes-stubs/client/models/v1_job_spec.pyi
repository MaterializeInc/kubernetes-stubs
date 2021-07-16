import datetime
import typing

import kubernetes.client

class V1JobSpec:
    active_deadline_seconds: typing.Optional[int]
    backoff_limit: typing.Optional[int]
    completions: typing.Optional[int]
    manual_selector: typing.Optional[bool]
    parallelism: typing.Optional[int]
    selector: typing.Optional[kubernetes.client.V1LabelSelector]
    template: kubernetes.client.V1PodTemplateSpec
    ttl_seconds_after_finished: typing.Optional[int]
    def __init__(
        self,
        *,
        active_deadline_seconds: typing.Optional[int] = ...,
        backoff_limit: typing.Optional[int] = ...,
        completions: typing.Optional[int] = ...,
        manual_selector: typing.Optional[bool] = ...,
        parallelism: typing.Optional[int] = ...,
        selector: typing.Optional[kubernetes.client.V1LabelSelector] = ...,
        template: kubernetes.client.V1PodTemplateSpec,
        ttl_seconds_after_finished: typing.Optional[int] = ...
    ) -> None: ...
