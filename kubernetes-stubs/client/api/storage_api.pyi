import typing

import kubernetes.client

class StorageApi:
    def get_api_group(self) -> kubernetes.client.V1APIGroup: ...
