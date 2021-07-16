import typing

import kubernetes.client

class CoreApi:
    def get_api_versions(self) -> kubernetes.client.V1APIVersions: ...
