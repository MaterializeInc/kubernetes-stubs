import datetime
import typing

import kubernetes.client

class ExtensionsV1beta1IngressBackend:
    service_name: str
    service_port: typing.Any
    def __init__(self, *, service_name: str, service_port: typing.Any) -> None: ...
