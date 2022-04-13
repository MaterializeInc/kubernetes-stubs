import datetime
import typing

import kubernetes.client

class V1beta1Subject:
    group: typing.Optional[kubernetes.client.V1beta1GroupSubject]
    kind: str
    service_account: typing.Optional[kubernetes.client.V1beta1ServiceAccountSubject]
    user: typing.Optional[kubernetes.client.V1beta1UserSubject]
    def __init__(
        self,
        *,
        group: typing.Optional[kubernetes.client.V1beta1GroupSubject] = ...,
        kind: str,
        service_account: typing.Optional[
            kubernetes.client.V1beta1ServiceAccountSubject
        ] = ...,
        user: typing.Optional[kubernetes.client.V1beta1UserSubject] = ...
    ) -> None: ...
    def to_dict(self) -> V1beta1SubjectDict: ...

class V1beta1SubjectDict(typing.TypedDict, total=False):
    group: typing.Optional[kubernetes.client.V1beta1GroupSubjectDict]
    kind: str
    serviceAccount: typing.Optional[kubernetes.client.V1beta1ServiceAccountSubjectDict]
    user: typing.Optional[kubernetes.client.V1beta1UserSubjectDict]
