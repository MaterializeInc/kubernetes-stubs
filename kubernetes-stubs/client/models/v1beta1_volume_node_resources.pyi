import datetime
import typing

import kubernetes.client

class V1beta1VolumeNodeResources:
    count: typing.Optional[int]
    def __init__(self, *, count: typing.Optional[int] = ...) -> None: ...
