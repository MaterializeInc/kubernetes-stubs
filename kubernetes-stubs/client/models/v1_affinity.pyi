import datetime
import typing

import kubernetes.client

class V1Affinity:
    node_affinity: typing.Optional[kubernetes.client.V1NodeAffinity]
    pod_affinity: typing.Optional[kubernetes.client.V1PodAffinity]
    pod_anti_affinity: typing.Optional[kubernetes.client.V1PodAntiAffinity]
    def __init__(
        self,
        *,
        node_affinity: typing.Optional[kubernetes.client.V1NodeAffinity] = ...,
        pod_affinity: typing.Optional[kubernetes.client.V1PodAffinity] = ...,
        pod_anti_affinity: typing.Optional[kubernetes.client.V1PodAntiAffinity] = ...
    ) -> None: ...
