import datetime
import typing

import kubernetes.client

class V1TokenReview:
    api_version: typing.Optional[str]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes.client.V1ObjectMeta]
    spec: kubernetes.client.V1TokenReviewSpec
    status: typing.Optional[kubernetes.client.V1TokenReviewStatus]
    def __init__(
        self,
        *,
        api_version: typing.Optional[str] = ...,
        kind: typing.Optional[str] = ...,
        metadata: typing.Optional[kubernetes.client.V1ObjectMeta] = ...,
        spec: kubernetes.client.V1TokenReviewSpec,
        status: typing.Optional[kubernetes.client.V1TokenReviewStatus] = ...
    ) -> None: ...
