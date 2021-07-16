import datetime
import typing

import kubernetes.client

class V1WeightedPodAffinityTerm:
    pod_affinity_term: kubernetes.client.V1PodAffinityTerm
    weight: int
    def __init__(
        self, *, pod_affinity_term: kubernetes.client.V1PodAffinityTerm, weight: int
    ) -> None: ...
