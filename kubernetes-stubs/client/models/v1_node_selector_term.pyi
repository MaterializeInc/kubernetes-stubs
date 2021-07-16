import datetime
import typing

import kubernetes.client

class V1NodeSelectorTerm:
    match_expressions: typing.Optional[
        list[kubernetes.client.V1NodeSelectorRequirement]
    ]
    match_fields: typing.Optional[list[kubernetes.client.V1NodeSelectorRequirement]]
    def __init__(
        self,
        *,
        match_expressions: typing.Optional[
            list[kubernetes.client.V1NodeSelectorRequirement]
        ] = ...,
        match_fields: typing.Optional[
            list[kubernetes.client.V1NodeSelectorRequirement]
        ] = ...
    ) -> None: ...
