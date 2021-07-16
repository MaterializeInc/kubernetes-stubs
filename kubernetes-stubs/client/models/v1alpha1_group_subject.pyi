import datetime
import typing

import kubernetes.client

class V1alpha1GroupSubject:
    name: str
    def __init__(self, *, name: str) -> None: ...
