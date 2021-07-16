import typing

import kubernetes.client

class NetworkingApi:
    def get_api_group(self) -> kubernetes.client.V1APIGroup: ...
