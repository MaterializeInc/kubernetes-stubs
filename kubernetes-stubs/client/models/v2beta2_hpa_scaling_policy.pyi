import datetime
import typing

import kubernetes.client

class V2beta2HPAScalingPolicy:
    period_seconds: int
    type: str
    value: int
    def __init__(self, *, period_seconds: int, type: str, value: int) -> None: ...
