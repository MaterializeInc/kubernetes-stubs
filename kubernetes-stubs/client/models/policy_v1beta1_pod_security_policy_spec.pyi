import datetime
import typing

import kubernetes.client

class PolicyV1beta1PodSecurityPolicySpec:
    allow_privilege_escalation: typing.Optional[bool]
    allowed_csi_drivers: typing.Optional[
        list[kubernetes.client.PolicyV1beta1AllowedCSIDriver]
    ]
    allowed_capabilities: typing.Optional[list[str]]
    allowed_flex_volumes: typing.Optional[
        list[kubernetes.client.PolicyV1beta1AllowedFlexVolume]
    ]
    allowed_host_paths: typing.Optional[
        list[kubernetes.client.PolicyV1beta1AllowedHostPath]
    ]
    allowed_proc_mount_types: typing.Optional[list[str]]
    allowed_unsafe_sysctls: typing.Optional[list[str]]
    default_add_capabilities: typing.Optional[list[str]]
    default_allow_privilege_escalation: typing.Optional[bool]
    forbidden_sysctls: typing.Optional[list[str]]
    fs_group: kubernetes.client.PolicyV1beta1FSGroupStrategyOptions
    host_ipc: typing.Optional[bool]
    host_network: typing.Optional[bool]
    host_pid: typing.Optional[bool]
    host_ports: typing.Optional[list[kubernetes.client.PolicyV1beta1HostPortRange]]
    privileged: typing.Optional[bool]
    read_only_root_filesystem: typing.Optional[bool]
    required_drop_capabilities: typing.Optional[list[str]]
    run_as_group: typing.Optional[
        kubernetes.client.PolicyV1beta1RunAsGroupStrategyOptions
    ]
    run_as_user: kubernetes.client.PolicyV1beta1RunAsUserStrategyOptions
    runtime_class: typing.Optional[
        kubernetes.client.PolicyV1beta1RuntimeClassStrategyOptions
    ]
    se_linux: kubernetes.client.PolicyV1beta1SELinuxStrategyOptions
    supplemental_groups: kubernetes.client.PolicyV1beta1SupplementalGroupsStrategyOptions
    volumes: typing.Optional[list[str]]
    def __init__(
        self,
        *,
        allow_privilege_escalation: typing.Optional[bool] = ...,
        allowed_csi_drivers: typing.Optional[
            list[kubernetes.client.PolicyV1beta1AllowedCSIDriver]
        ] = ...,
        allowed_capabilities: typing.Optional[list[str]] = ...,
        allowed_flex_volumes: typing.Optional[
            list[kubernetes.client.PolicyV1beta1AllowedFlexVolume]
        ] = ...,
        allowed_host_paths: typing.Optional[
            list[kubernetes.client.PolicyV1beta1AllowedHostPath]
        ] = ...,
        allowed_proc_mount_types: typing.Optional[list[str]] = ...,
        allowed_unsafe_sysctls: typing.Optional[list[str]] = ...,
        default_add_capabilities: typing.Optional[list[str]] = ...,
        default_allow_privilege_escalation: typing.Optional[bool] = ...,
        forbidden_sysctls: typing.Optional[list[str]] = ...,
        fs_group: kubernetes.client.PolicyV1beta1FSGroupStrategyOptions,
        host_ipc: typing.Optional[bool] = ...,
        host_network: typing.Optional[bool] = ...,
        host_pid: typing.Optional[bool] = ...,
        host_ports: typing.Optional[
            list[kubernetes.client.PolicyV1beta1HostPortRange]
        ] = ...,
        privileged: typing.Optional[bool] = ...,
        read_only_root_filesystem: typing.Optional[bool] = ...,
        required_drop_capabilities: typing.Optional[list[str]] = ...,
        run_as_group: typing.Optional[
            kubernetes.client.PolicyV1beta1RunAsGroupStrategyOptions
        ] = ...,
        run_as_user: kubernetes.client.PolicyV1beta1RunAsUserStrategyOptions,
        runtime_class: typing.Optional[
            kubernetes.client.PolicyV1beta1RuntimeClassStrategyOptions
        ] = ...,
        se_linux: kubernetes.client.PolicyV1beta1SELinuxStrategyOptions,
        supplemental_groups: kubernetes.client.PolicyV1beta1SupplementalGroupsStrategyOptions,
        volumes: typing.Optional[list[str]] = ...
    ) -> None: ...
