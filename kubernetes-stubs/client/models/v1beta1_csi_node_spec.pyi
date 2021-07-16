import datetime
import typing

import kubernetes.client

class V1beta1CSINodeSpec:
    drivers: list[kubernetes.client.V1beta1CSINodeDriver]
    def __init__(
        self, *, drivers: list[kubernetes.client.V1beta1CSINodeDriver]
    ) -> None: ...
