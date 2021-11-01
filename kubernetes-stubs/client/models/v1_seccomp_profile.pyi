import datetime
import typing

import kubernetes.client

class V1SeccompProfile:
    localhost_profile: typing.Optional[str]
    type: str
    def __init__(
        self, *, localhost_profile: typing.Optional[str] = ..., type: str
    ) -> None: ...
    def to_dict(self) -> V1SeccompProfileDict: ...

class V1SeccompProfileDict(typing.TypedDict, total=False):
    localhostProfile: typing.Optional[str]
    type: str
