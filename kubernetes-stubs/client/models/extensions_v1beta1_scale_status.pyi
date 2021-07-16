import datetime
import typing

import kubernetes.client

class ExtensionsV1beta1ScaleStatus:
    replicas: int
    selector: typing.Optional[dict[str, str]]
    target_selector: typing.Optional[str]
    def __init__(
        self,
        *,
        replicas: int,
        selector: typing.Optional[dict[str, str]] = ...,
        target_selector: typing.Optional[str] = ...
    ) -> None: ...
