import datetime
import typing

import kubernetes.client

class V1beta3FlowDistinguisherMethod:
    type: str
    def __init__(self, *, type: str) -> None: ...
    def to_dict(self) -> V1beta3FlowDistinguisherMethodDict: ...

class V1beta3FlowDistinguisherMethodDict(typing.TypedDict, total=False):
    type: str
