import datetime
import typing

import kubernetes.client

class V1DownwardAPIProjection:
    items: typing.Optional[list[kubernetes.client.V1DownwardAPIVolumeFile]]
    def __init__(
        self,
        *,
        items: typing.Optional[list[kubernetes.client.V1DownwardAPIVolumeFile]] = ...
    ) -> None: ...
