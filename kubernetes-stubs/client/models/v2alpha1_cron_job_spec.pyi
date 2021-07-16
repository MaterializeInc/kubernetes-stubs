import datetime
import typing

import kubernetes.client

class V2alpha1CronJobSpec:
    concurrency_policy: typing.Optional[str]
    failed_jobs_history_limit: typing.Optional[int]
    job_template: kubernetes.client.V2alpha1JobTemplateSpec
    schedule: str
    starting_deadline_seconds: typing.Optional[int]
    successful_jobs_history_limit: typing.Optional[int]
    suspend: typing.Optional[bool]
    def __init__(
        self,
        *,
        concurrency_policy: typing.Optional[str] = ...,
        failed_jobs_history_limit: typing.Optional[int] = ...,
        job_template: kubernetes.client.V2alpha1JobTemplateSpec,
        schedule: str,
        starting_deadline_seconds: typing.Optional[int] = ...,
        successful_jobs_history_limit: typing.Optional[int] = ...,
        suspend: typing.Optional[bool] = ...
    ) -> None: ...
