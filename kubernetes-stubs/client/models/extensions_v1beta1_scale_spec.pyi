import datetime
import typing

import kubernetes.client

class ExtensionsV1beta1ScaleSpec:
    replicas: typing.Optional[int]
    def __init__(self, *, replicas: typing.Optional[int] = ...) -> None: ...
