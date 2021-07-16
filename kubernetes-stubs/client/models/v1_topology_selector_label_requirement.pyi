import datetime
import typing

import kubernetes.client

class V1TopologySelectorLabelRequirement:
    key: str
    values: list[str]
    def __init__(self, *, key: str, values: list[str]) -> None: ...
