import typing

import kubernetes.client

class FlowcontrolApiserverApi:
    def get_api_group(self) -> kubernetes.client.V1APIGroup: ...
