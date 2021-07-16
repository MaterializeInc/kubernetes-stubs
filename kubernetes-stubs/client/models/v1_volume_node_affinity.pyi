import datetime
import typing

import kubernetes.client

class V1VolumeNodeAffinity:
    required: typing.Optional[kubernetes.client.V1NodeSelector]
    def __init__(
        self, *, required: typing.Optional[kubernetes.client.V1NodeSelector] = ...
    ) -> None: ...
