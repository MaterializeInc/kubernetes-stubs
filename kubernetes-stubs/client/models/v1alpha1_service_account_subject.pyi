import datetime
import typing

import kubernetes.client

class V1alpha1ServiceAccountSubject:
    name: str
    namespace: str
    def __init__(self, *, name: str, namespace: str) -> None: ...
