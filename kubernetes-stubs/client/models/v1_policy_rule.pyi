import datetime
import typing

import kubernetes.client

class V1PolicyRule:
    api_groups: typing.Optional[list[str]]
    non_resource_ur_ls: typing.Optional[list[str]]
    resource_names: typing.Optional[list[str]]
    resources: typing.Optional[list[str]]
    verbs: list[str]
    def __init__(
        self,
        *,
        api_groups: typing.Optional[list[str]] = ...,
        non_resource_ur_ls: typing.Optional[list[str]] = ...,
        resource_names: typing.Optional[list[str]] = ...,
        resources: typing.Optional[list[str]] = ...,
        verbs: list[str]
    ) -> None: ...
