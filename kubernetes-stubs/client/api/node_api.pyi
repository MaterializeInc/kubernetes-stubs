import typing

import kubernetes.client

class NodeApi:
    def get_api_group(self) -> kubernetes.client.V1APIGroup: ...
