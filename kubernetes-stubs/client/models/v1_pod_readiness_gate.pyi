import datetime
import typing

import kubernetes.client

class V1PodReadinessGate:
    condition_type: str
    def __init__(self, *, condition_type: str) -> None: ...
