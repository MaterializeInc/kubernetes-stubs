from typing import Optional

from kubernetes.client import Configuration

class ApiClient:
    def __init__(self, configuration: Optional[Configuration]) -> None: ...
