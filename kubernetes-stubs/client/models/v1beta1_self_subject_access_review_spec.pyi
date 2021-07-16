import datetime
import typing

import kubernetes.client

class V1beta1SelfSubjectAccessReviewSpec:
    non_resource_attributes: typing.Optional[
        kubernetes.client.V1beta1NonResourceAttributes
    ]
    resource_attributes: typing.Optional[kubernetes.client.V1beta1ResourceAttributes]
    def __init__(
        self,
        *,
        non_resource_attributes: typing.Optional[
            kubernetes.client.V1beta1NonResourceAttributes
        ] = ...,
        resource_attributes: typing.Optional[
            kubernetes.client.V1beta1ResourceAttributes
        ] = ...
    ) -> None: ...
