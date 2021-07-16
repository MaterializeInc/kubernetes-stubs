import datetime
import typing

import kubernetes.client

class V1alpha1PriorityLevelConfigurationReference:
    name: str
    def __init__(self, *, name: str) -> None: ...
