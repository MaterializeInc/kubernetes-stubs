import datetime
import typing

import kubernetes.client

class V1beta1RuntimeClassStrategyOptions:
    allowed_runtime_class_names: list[str]
    default_runtime_class_name: typing.Optional[str]
    def __init__(
        self,
        *,
        allowed_runtime_class_names: list[str],
        default_runtime_class_name: typing.Optional[str] = ...
    ) -> None: ...
