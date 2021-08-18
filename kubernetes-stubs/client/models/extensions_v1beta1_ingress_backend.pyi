import datetime
import typing

import kubernetes.client

class ExtensionsV1beta1IngressBackend:
    resource: typing.Optional[kubernetes.client.V1TypedLocalObjectReference]
    service_name: typing.Optional[str]
    service_port: typing.Optional[typing.Any]
    def __init__(
        self,
        *,
        resource: typing.Optional[kubernetes.client.V1TypedLocalObjectReference] = ...,
        service_name: typing.Optional[str] = ...,
        service_port: typing.Optional[typing.Any] = ...
    ) -> None: ...
