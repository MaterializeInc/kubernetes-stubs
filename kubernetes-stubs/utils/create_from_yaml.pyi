import typing
from kubernetes.client import ApiClient

def create_from_yaml(
    k8s_client: ApiClient,
    yaml_file: str = None,
    yaml_objects: typing.List[dict] = None,
    verbose: bool = False,
    namespace: str = "default",
    *,
    async_req: typing.Optional[bool] = ...,
    include_uninitialized: typing.Optional[bool] = ...,
    pretty: typing.Optional[str] = ...,
    dry_run: typing.Optional[str] = ...,
) -> typing.List[typing.Any]: ...
