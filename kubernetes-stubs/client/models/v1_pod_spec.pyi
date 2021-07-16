import datetime
import typing

import kubernetes.client

class V1PodSpec:
    active_deadline_seconds: typing.Optional[int]
    affinity: typing.Optional[kubernetes.client.V1Affinity]
    automount_service_account_token: typing.Optional[bool]
    containers: list[kubernetes.client.V1Container]
    dns_config: typing.Optional[kubernetes.client.V1PodDNSConfig]
    dns_policy: typing.Optional[str]
    enable_service_links: typing.Optional[bool]
    ephemeral_containers: typing.Optional[list[kubernetes.client.V1EphemeralContainer]]
    host_aliases: typing.Optional[list[kubernetes.client.V1HostAlias]]
    host_ipc: typing.Optional[bool]
    host_network: typing.Optional[bool]
    host_pid: typing.Optional[bool]
    hostname: typing.Optional[str]
    image_pull_secrets: typing.Optional[list[kubernetes.client.V1LocalObjectReference]]
    init_containers: typing.Optional[list[kubernetes.client.V1Container]]
    node_name: typing.Optional[str]
    node_selector: typing.Optional[dict[str, str]]
    overhead: typing.Optional[dict[str, str]]
    preemption_policy: typing.Optional[str]
    priority: typing.Optional[int]
    priority_class_name: typing.Optional[str]
    readiness_gates: typing.Optional[list[kubernetes.client.V1PodReadinessGate]]
    restart_policy: typing.Optional[str]
    runtime_class_name: typing.Optional[str]
    scheduler_name: typing.Optional[str]
    security_context: typing.Optional[kubernetes.client.V1PodSecurityContext]
    service_account: typing.Optional[str]
    service_account_name: typing.Optional[str]
    share_process_namespace: typing.Optional[bool]
    subdomain: typing.Optional[str]
    termination_grace_period_seconds: typing.Optional[int]
    tolerations: typing.Optional[list[kubernetes.client.V1Toleration]]
    topology_spread_constraints: typing.Optional[
        list[kubernetes.client.V1TopologySpreadConstraint]
    ]
    volumes: typing.Optional[list[kubernetes.client.V1Volume]]
    def __init__(
        self,
        *,
        active_deadline_seconds: typing.Optional[int] = ...,
        affinity: typing.Optional[kubernetes.client.V1Affinity] = ...,
        automount_service_account_token: typing.Optional[bool] = ...,
        containers: list[kubernetes.client.V1Container],
        dns_config: typing.Optional[kubernetes.client.V1PodDNSConfig] = ...,
        dns_policy: typing.Optional[str] = ...,
        enable_service_links: typing.Optional[bool] = ...,
        ephemeral_containers: typing.Optional[
            list[kubernetes.client.V1EphemeralContainer]
        ] = ...,
        host_aliases: typing.Optional[list[kubernetes.client.V1HostAlias]] = ...,
        host_ipc: typing.Optional[bool] = ...,
        host_network: typing.Optional[bool] = ...,
        host_pid: typing.Optional[bool] = ...,
        hostname: typing.Optional[str] = ...,
        image_pull_secrets: typing.Optional[
            list[kubernetes.client.V1LocalObjectReference]
        ] = ...,
        init_containers: typing.Optional[list[kubernetes.client.V1Container]] = ...,
        node_name: typing.Optional[str] = ...,
        node_selector: typing.Optional[dict[str, str]] = ...,
        overhead: typing.Optional[dict[str, str]] = ...,
        preemption_policy: typing.Optional[str] = ...,
        priority: typing.Optional[int] = ...,
        priority_class_name: typing.Optional[str] = ...,
        readiness_gates: typing.Optional[
            list[kubernetes.client.V1PodReadinessGate]
        ] = ...,
        restart_policy: typing.Optional[str] = ...,
        runtime_class_name: typing.Optional[str] = ...,
        scheduler_name: typing.Optional[str] = ...,
        security_context: typing.Optional[kubernetes.client.V1PodSecurityContext] = ...,
        service_account: typing.Optional[str] = ...,
        service_account_name: typing.Optional[str] = ...,
        share_process_namespace: typing.Optional[bool] = ...,
        subdomain: typing.Optional[str] = ...,
        termination_grace_period_seconds: typing.Optional[int] = ...,
        tolerations: typing.Optional[list[kubernetes.client.V1Toleration]] = ...,
        topology_spread_constraints: typing.Optional[
            list[kubernetes.client.V1TopologySpreadConstraint]
        ] = ...,
        volumes: typing.Optional[list[kubernetes.client.V1Volume]] = ...
    ) -> None: ...
