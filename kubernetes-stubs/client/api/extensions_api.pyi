import typing

import kubernetes.client

class ExtensionsApi:
    def get_api_group(self) -> kubernetes.client.V1APIGroup: ...
