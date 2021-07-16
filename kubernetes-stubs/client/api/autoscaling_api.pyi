import typing

import kubernetes.client

class AutoscalingApi:
    def get_api_group(self) -> kubernetes.client.V1APIGroup: ...
