import datetime
import typing

import kubernetes.client

class V1EphemeralVolumeSource:
    read_only: typing.Optional[bool]
    volume_claim_template: typing.Optional[
        kubernetes.client.V1PersistentVolumeClaimTemplate
    ]
    def __init__(
        self,
        *,
        read_only: typing.Optional[bool] = ...,
        volume_claim_template: typing.Optional[
            kubernetes.client.V1PersistentVolumeClaimTemplate
        ] = ...
    ) -> None: ...
    def to_dict(self) -> V1EphemeralVolumeSourceDict: ...

class V1EphemeralVolumeSourceDict(typing.TypedDict, total=False):
    readOnly: typing.Optional[bool]
    volumeClaimTemplate: typing.Optional[
        kubernetes.client.V1PersistentVolumeClaimTemplateDict
    ]
