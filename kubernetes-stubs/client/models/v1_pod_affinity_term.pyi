import datetime
import typing

import kubernetes.client

class V1PodAffinityTerm:
    label_selector: typing.Optional[kubernetes.client.V1LabelSelector]
    namespaces: typing.Optional[list[str]]
    topology_key: str
    def __init__(
        self,
        *,
        label_selector: typing.Optional[kubernetes.client.V1LabelSelector] = ...,
        namespaces: typing.Optional[list[str]] = ...,
        topology_key: str
    ) -> None: ...
