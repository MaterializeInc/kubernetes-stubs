import datetime
import typing

import kubernetes.client

class V1beta1CustomResourceSubresources:
    scale: typing.Optional[kubernetes.client.V1beta1CustomResourceSubresourceScale]
    status: typing.Optional[typing.Any]
    def __init__(
        self,
        *,
        scale: typing.Optional[
            kubernetes.client.V1beta1CustomResourceSubresourceScale
        ] = ...,
        status: typing.Optional[typing.Any] = ...
    ) -> None: ...
