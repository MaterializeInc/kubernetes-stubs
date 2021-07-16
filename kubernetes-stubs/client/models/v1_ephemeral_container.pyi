import datetime
import typing

import kubernetes.client

class V1EphemeralContainer:
    args: typing.Optional[list[str]]
    command: typing.Optional[list[str]]
    env: typing.Optional[list[kubernetes.client.V1EnvVar]]
    env_from: typing.Optional[list[kubernetes.client.V1EnvFromSource]]
    image: typing.Optional[str]
    image_pull_policy: typing.Optional[str]
    lifecycle: typing.Optional[kubernetes.client.V1Lifecycle]
    liveness_probe: typing.Optional[kubernetes.client.V1Probe]
    name: str
    ports: typing.Optional[list[kubernetes.client.V1ContainerPort]]
    readiness_probe: typing.Optional[kubernetes.client.V1Probe]
    resources: typing.Optional[kubernetes.client.V1ResourceRequirements]
    security_context: typing.Optional[kubernetes.client.V1SecurityContext]
    startup_probe: typing.Optional[kubernetes.client.V1Probe]
    stdin: typing.Optional[bool]
    stdin_once: typing.Optional[bool]
    target_container_name: typing.Optional[str]
    termination_message_path: typing.Optional[str]
    termination_message_policy: typing.Optional[str]
    tty: typing.Optional[bool]
    volume_devices: typing.Optional[list[kubernetes.client.V1VolumeDevice]]
    volume_mounts: typing.Optional[list[kubernetes.client.V1VolumeMount]]
    working_dir: typing.Optional[str]
    def __init__(
        self,
        *,
        args: typing.Optional[list[str]] = ...,
        command: typing.Optional[list[str]] = ...,
        env: typing.Optional[list[kubernetes.client.V1EnvVar]] = ...,
        env_from: typing.Optional[list[kubernetes.client.V1EnvFromSource]] = ...,
        image: typing.Optional[str] = ...,
        image_pull_policy: typing.Optional[str] = ...,
        lifecycle: typing.Optional[kubernetes.client.V1Lifecycle] = ...,
        liveness_probe: typing.Optional[kubernetes.client.V1Probe] = ...,
        name: str,
        ports: typing.Optional[list[kubernetes.client.V1ContainerPort]] = ...,
        readiness_probe: typing.Optional[kubernetes.client.V1Probe] = ...,
        resources: typing.Optional[kubernetes.client.V1ResourceRequirements] = ...,
        security_context: typing.Optional[kubernetes.client.V1SecurityContext] = ...,
        startup_probe: typing.Optional[kubernetes.client.V1Probe] = ...,
        stdin: typing.Optional[bool] = ...,
        stdin_once: typing.Optional[bool] = ...,
        target_container_name: typing.Optional[str] = ...,
        termination_message_path: typing.Optional[str] = ...,
        termination_message_policy: typing.Optional[str] = ...,
        tty: typing.Optional[bool] = ...,
        volume_devices: typing.Optional[list[kubernetes.client.V1VolumeDevice]] = ...,
        volume_mounts: typing.Optional[list[kubernetes.client.V1VolumeMount]] = ...,
        working_dir: typing.Optional[str] = ...
    ) -> None: ...
