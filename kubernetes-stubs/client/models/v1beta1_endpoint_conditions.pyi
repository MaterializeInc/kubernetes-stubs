import datetime
import typing

import kubernetes.client

class V1beta1EndpointConditions:
    ready: typing.Optional[bool]
    def __init__(self, *, ready: typing.Optional[bool] = ...) -> None: ...
