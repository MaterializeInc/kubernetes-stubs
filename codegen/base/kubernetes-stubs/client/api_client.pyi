from typing import Optional, Type, TypeVar

from kubernetes.client import Configuration

_T = TypeVar("_T")

class ApiClient:
    def __init__(self, configuration: Optional[Configuration] = ...) -> None: ...
    def __deserialize(self, response: str, response_type: Type[_T]) -> _T: ...
