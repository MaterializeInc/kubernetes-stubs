import datetime
import typing

import kubernetes.client

class V1NonResourceRule:
    non_resource_ur_ls: typing.Optional[list[str]]
    verbs: list[str]
    def __init__(
        self, *, non_resource_ur_ls: typing.Optional[list[str]] = ..., verbs: list[str]
    ) -> None: ...
