import datetime
import typing

import kubernetes.client

class V1NodeSelectorRequirement:
    key: str
    operator: str
    values: typing.Optional[list[str]]
    def __init__(
        self, *, key: str, operator: str, values: typing.Optional[list[str]] = ...
    ) -> None: ...
