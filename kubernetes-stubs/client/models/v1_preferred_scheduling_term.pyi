import datetime
import typing

import kubernetes.client

class V1PreferredSchedulingTerm:
    preference: kubernetes.client.V1NodeSelectorTerm
    weight: int
    def __init__(
        self, *, preference: kubernetes.client.V1NodeSelectorTerm, weight: int
    ) -> None: ...
