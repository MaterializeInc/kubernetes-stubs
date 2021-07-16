import datetime
import typing

import kubernetes.client

class V1GroupVersionForDiscovery:
    group_version: str
    version: str
    def __init__(self, *, group_version: str, version: str) -> None: ...
