import datetime
import typing

import kubernetes.client

class V1NodeSystemInfo:
    architecture: str
    boot_id: str
    container_runtime_version: str
    kernel_version: str
    kube_proxy_version: str
    kubelet_version: str
    machine_id: str
    operating_system: str
    os_image: str
    system_uuid: str
    def __init__(
        self,
        *,
        architecture: str,
        boot_id: str,
        container_runtime_version: str,
        kernel_version: str,
        kube_proxy_version: str,
        kubelet_version: str,
        machine_id: str,
        operating_system: str,
        os_image: str,
        system_uuid: str
    ) -> None: ...
