import datetime
import typing

import kubernetes.client

class V1beta2ScaleSpec:
    replicas: typing.Optional[int]
    def __init__(self, *, replicas: typing.Optional[int] = ...) -> None: ...
