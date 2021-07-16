import typing

import kubernetes.client

class CoordinationApi:
    def get_api_group(self) -> kubernetes.client.V1APIGroup: ...
