import datetime
import typing

import kubernetes.client

class V1beta1FlowDistinguisherMethod:
    type: str
    def __init__(self, *, type: str) -> None: ...
    def to_dict(self) -> V1beta1FlowDistinguisherMethodDict: ...

class V1beta1FlowDistinguisherMethodDict(typing.TypedDict, total=False):
    type: str
