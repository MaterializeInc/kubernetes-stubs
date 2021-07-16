import datetime
import typing

import kubernetes.client

class V1beta1SubjectAccessReviewSpec:
    extra: typing.Optional[dict[str, list[str]]]
    group: typing.Optional[list[str]]
    non_resource_attributes: typing.Optional[
        kubernetes.client.V1beta1NonResourceAttributes
    ]
    resource_attributes: typing.Optional[kubernetes.client.V1beta1ResourceAttributes]
    uid: typing.Optional[str]
    user: typing.Optional[str]
    def __init__(
        self,
        *,
        extra: typing.Optional[dict[str, list[str]]] = ...,
        group: typing.Optional[list[str]] = ...,
        non_resource_attributes: typing.Optional[
            kubernetes.client.V1beta1NonResourceAttributes
        ] = ...,
        resource_attributes: typing.Optional[
            kubernetes.client.V1beta1ResourceAttributes
        ] = ...,
        uid: typing.Optional[str] = ...,
        user: typing.Optional[str] = ...
    ) -> None: ...
