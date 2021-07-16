import datetime
import typing

import kubernetes.client

class V1alpha1Policy:
    level: str
    stages: typing.Optional[list[str]]
    def __init__(
        self, *, level: str, stages: typing.Optional[list[str]] = ...
    ) -> None: ...
