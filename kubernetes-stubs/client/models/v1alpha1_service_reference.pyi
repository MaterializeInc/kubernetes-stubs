import datetime
import typing

import kubernetes.client

class V1alpha1ServiceReference:
    name: str
    namespace: str
    path: typing.Optional[str]
    port: typing.Optional[int]
    def __init__(
        self,
        *,
        name: str,
        namespace: str,
        path: typing.Optional[str] = ...,
        port: typing.Optional[int] = ...
    ) -> None: ...
