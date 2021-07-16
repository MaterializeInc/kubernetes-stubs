import typing

import kubernetes.client

class PolicyApi:
    def get_api_group(self) -> kubernetes.client.V1APIGroup: ...
