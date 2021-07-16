import datetime
import typing

import kubernetes.client

class V1ScopedResourceSelectorRequirement:
    operator: str
    scope_name: str
    values: typing.Optional[list[str]]
    def __init__(
        self,
        *,
        operator: str,
        scope_name: str,
        values: typing.Optional[list[str]] = ...
    ) -> None: ...
