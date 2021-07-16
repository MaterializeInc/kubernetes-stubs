import datetime
import typing

import kubernetes.client

class V1NodeStatus:
    addresses: typing.Optional[list[kubernetes.client.V1NodeAddress]]
    allocatable: typing.Optional[dict[str, str]]
    capacity: typing.Optional[dict[str, str]]
    conditions: typing.Optional[list[kubernetes.client.V1NodeCondition]]
    config: typing.Optional[kubernetes.client.V1NodeConfigStatus]
    daemon_endpoints: typing.Optional[kubernetes.client.V1NodeDaemonEndpoints]
    images: typing.Optional[list[kubernetes.client.V1ContainerImage]]
    node_info: typing.Optional[kubernetes.client.V1NodeSystemInfo]
    phase: typing.Optional[str]
    volumes_attached: typing.Optional[list[kubernetes.client.V1AttachedVolume]]
    volumes_in_use: typing.Optional[list[str]]
    def __init__(
        self,
        *,
        addresses: typing.Optional[list[kubernetes.client.V1NodeAddress]] = ...,
        allocatable: typing.Optional[dict[str, str]] = ...,
        capacity: typing.Optional[dict[str, str]] = ...,
        conditions: typing.Optional[list[kubernetes.client.V1NodeCondition]] = ...,
        config: typing.Optional[kubernetes.client.V1NodeConfigStatus] = ...,
        daemon_endpoints: typing.Optional[
            kubernetes.client.V1NodeDaemonEndpoints
        ] = ...,
        images: typing.Optional[list[kubernetes.client.V1ContainerImage]] = ...,
        node_info: typing.Optional[kubernetes.client.V1NodeSystemInfo] = ...,
        phase: typing.Optional[str] = ...,
        volumes_attached: typing.Optional[
            list[kubernetes.client.V1AttachedVolume]
        ] = ...,
        volumes_in_use: typing.Optional[list[str]] = ...
    ) -> None: ...
