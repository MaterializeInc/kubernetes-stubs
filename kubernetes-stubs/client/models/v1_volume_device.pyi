import datetime
import typing

import kubernetes.client

class V1VolumeDevice:
    device_path: str
    name: str
    def __init__(self, *, device_path: str, name: str) -> None: ...
