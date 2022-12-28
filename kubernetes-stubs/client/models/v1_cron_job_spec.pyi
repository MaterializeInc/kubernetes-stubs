import datetime
import typing

import kubernetes.client

class V1CronJobSpec:
    concurrency_policy: typing.Optional[str]
    failed_jobs_history_limit: typing.Optional[int]
    job_template: kubernetes.client.V1JobTemplateSpec
    schedule: str
    starting_deadline_seconds: typing.Optional[int]
    successful_jobs_history_limit: typing.Optional[int]
    suspend: typing.Optional[bool]

    def __init__(
        self,
        *,
        concurrency_policy: typing.Optional[str] = ...,
        failed_jobs_history_limit: typing.Optional[int] = ...,
        job_template: kubernetes.client.V1JobTemplateSpec,
        schedule: str,
        starting_deadline_seconds: typing.Optional[int] = ...,
        successful_jobs_history_limit: typing.Optional[int] = ...,
        suspend: typing.Optional[bool] = ...
    ) -> None: ...
    def to_dict(self) -> V1CronJobSpecDict: ...

class V1CronJobSpecDict(typing.TypedDict, total=False):
    concurrencyPolicy: typing.Optional[str]
    failedJobsHistoryLimit: typing.Optional[int]
    jobTemplate: kubernetes.client.V1JobTemplateSpecDict
    schedule: str
    startingDeadlineSeconds: typing.Optional[int]
    successfulJobsHistoryLimit: typing.Optional[int]
    suspend: typing.Optional[bool]
