import datetime
import typing

import kubernetes.client

class V1alpha1UserSubject:
    name: str
    def __init__(self, *, name: str) -> None: ...
