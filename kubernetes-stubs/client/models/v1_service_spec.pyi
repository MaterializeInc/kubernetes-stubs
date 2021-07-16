import datetime
import typing

import kubernetes.client

class V1ServiceSpec:
    cluster_ip: typing.Optional[str]
    external_i_ps: typing.Optional[list[str]]
    external_name: typing.Optional[str]
    external_traffic_policy: typing.Optional[str]
    health_check_node_port: typing.Optional[int]
    ip_family: typing.Optional[str]
    load_balancer_ip: typing.Optional[str]
    load_balancer_source_ranges: typing.Optional[list[str]]
    ports: typing.Optional[list[kubernetes.client.V1ServicePort]]
    publish_not_ready_addresses: typing.Optional[bool]
    selector: typing.Optional[dict[str, str]]
    session_affinity: typing.Optional[str]
    session_affinity_config: typing.Optional[kubernetes.client.V1SessionAffinityConfig]
    topology_keys: typing.Optional[list[str]]
    type: typing.Optional[str]
    def __init__(
        self,
        *,
        cluster_ip: typing.Optional[str] = ...,
        external_i_ps: typing.Optional[list[str]] = ...,
        external_name: typing.Optional[str] = ...,
        external_traffic_policy: typing.Optional[str] = ...,
        health_check_node_port: typing.Optional[int] = ...,
        ip_family: typing.Optional[str] = ...,
        load_balancer_ip: typing.Optional[str] = ...,
        load_balancer_source_ranges: typing.Optional[list[str]] = ...,
        ports: typing.Optional[list[kubernetes.client.V1ServicePort]] = ...,
        publish_not_ready_addresses: typing.Optional[bool] = ...,
        selector: typing.Optional[dict[str, str]] = ...,
        session_affinity: typing.Optional[str] = ...,
        session_affinity_config: typing.Optional[
            kubernetes.client.V1SessionAffinityConfig
        ] = ...,
        topology_keys: typing.Optional[list[str]] = ...,
        type: typing.Optional[str] = ...
    ) -> None: ...
