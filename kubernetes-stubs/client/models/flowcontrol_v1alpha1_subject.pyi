import datetime
import typing

import kubernetes.client

class FlowcontrolV1alpha1Subject:
    group: typing.Optional[kubernetes.client.V1alpha1GroupSubject]
    kind: str
    service_account: typing.Optional[kubernetes.client.V1alpha1ServiceAccountSubject]
    user: typing.Optional[kubernetes.client.V1alpha1UserSubject]
    def __init__(
        self,
        *,
        group: typing.Optional[kubernetes.client.V1alpha1GroupSubject] = ...,
        kind: str,
        service_account: typing.Optional[
            kubernetes.client.V1alpha1ServiceAccountSubject
        ] = ...,
        user: typing.Optional[kubernetes.client.V1alpha1UserSubject] = ...
    ) -> None: ...
