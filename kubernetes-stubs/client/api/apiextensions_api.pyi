import typing

import kubernetes.client

class ApiextensionsApi:
    def get_api_group(self) -> kubernetes.client.V1APIGroup: ...
