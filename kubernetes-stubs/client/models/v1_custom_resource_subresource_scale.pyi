import datetime
import typing

import kubernetes.client

class V1CustomResourceSubresourceScale:
    label_selector_path: typing.Optional[str]
    spec_replicas_path: str
    status_replicas_path: str
    def __init__(
        self,
        *,
        label_selector_path: typing.Optional[str] = ...,
        spec_replicas_path: str,
        status_replicas_path: str
    ) -> None: ...
