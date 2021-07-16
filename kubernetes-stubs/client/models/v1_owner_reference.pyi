import datetime
import typing

import kubernetes.client

class V1OwnerReference:
    api_version: str
    block_owner_deletion: typing.Optional[bool]
    controller: typing.Optional[bool]
    kind: str
    name: str
    uid: str
    def __init__(
        self,
        *,
        api_version: str,
        block_owner_deletion: typing.Optional[bool] = ...,
        controller: typing.Optional[bool] = ...,
        kind: str,
        name: str,
        uid: str
    ) -> None: ...
