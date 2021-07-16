import datetime
import typing

import kubernetes.client

class V1DaemonEndpoint:
    port: int
    def __init__(self, *, port: int) -> None: ...
