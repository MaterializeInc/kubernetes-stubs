import typing

import kubernetes.client

class DiscoveryApi:
    def get_api_group(self) -> kubernetes.client.V1APIGroup: ...
