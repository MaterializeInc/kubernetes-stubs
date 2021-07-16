import typing

import kubernetes.client

class BatchApi:
    def get_api_group(self) -> kubernetes.client.V1APIGroup: ...
