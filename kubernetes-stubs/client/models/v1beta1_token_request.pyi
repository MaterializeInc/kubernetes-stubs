import datetime
import typing

import kubernetes.client

class V1beta1TokenRequest:
    audience: str
    expiration_seconds: typing.Optional[int]
    def __init__(
        self, *, audience: str, expiration_seconds: typing.Optional[int] = ...
    ) -> None: ...
    def to_dict(self) -> V1beta1TokenRequestDict: ...

class V1beta1TokenRequestDict(typing.TypedDict, total=False):
    audience: str
    expirationSeconds: typing.Optional[int]
