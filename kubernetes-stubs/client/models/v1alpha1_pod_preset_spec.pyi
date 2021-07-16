import datetime
import typing

import kubernetes.client

class V1alpha1PodPresetSpec:
    env: typing.Optional[list[kubernetes.client.V1EnvVar]]
    env_from: typing.Optional[list[kubernetes.client.V1EnvFromSource]]
    selector: typing.Optional[kubernetes.client.V1LabelSelector]
    volume_mounts: typing.Optional[list[kubernetes.client.V1VolumeMount]]
    volumes: typing.Optional[list[kubernetes.client.V1Volume]]
    def __init__(
        self,
        *,
        env: typing.Optional[list[kubernetes.client.V1EnvVar]] = ...,
        env_from: typing.Optional[list[kubernetes.client.V1EnvFromSource]] = ...,
        selector: typing.Optional[kubernetes.client.V1LabelSelector] = ...,
        volume_mounts: typing.Optional[list[kubernetes.client.V1VolumeMount]] = ...,
        volumes: typing.Optional[list[kubernetes.client.V1Volume]] = ...
    ) -> None: ...
