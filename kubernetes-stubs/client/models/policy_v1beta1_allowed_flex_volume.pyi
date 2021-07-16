import datetime
import typing

import kubernetes.client

class PolicyV1beta1AllowedFlexVolume:
    driver: str
    def __init__(self, *, driver: str) -> None: ...
