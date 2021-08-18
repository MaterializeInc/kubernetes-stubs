import datetime
import typing

import kubernetes.client

class V1beta1AllowedFlexVolume:
    driver: str
    def __init__(self, *, driver: str) -> None: ...
