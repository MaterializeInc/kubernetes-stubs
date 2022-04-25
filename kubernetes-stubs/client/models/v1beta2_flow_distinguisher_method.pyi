import datetime
import typing

import kubernetes.client

class V1beta2FlowDistinguisherMethod:
    type: str
    def __init__(self, *, type: str) -> None: ...
    def to_dict(self) -> V1beta2FlowDistinguisherMethodDict: ...

class V1beta2FlowDistinguisherMethodDict(typing.TypedDict, total=False):
    type: str
