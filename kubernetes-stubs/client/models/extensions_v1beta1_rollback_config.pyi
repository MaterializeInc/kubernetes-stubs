import datetime
import typing

import kubernetes.client

class ExtensionsV1beta1RollbackConfig:
    revision: typing.Optional[int]
    def __init__(self, *, revision: typing.Optional[int] = ...) -> None: ...
