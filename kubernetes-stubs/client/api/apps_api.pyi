import typing

import kubernetes.client

class AppsApi:
    def get_api_group(self) -> kubernetes.client.V1APIGroup: ...
