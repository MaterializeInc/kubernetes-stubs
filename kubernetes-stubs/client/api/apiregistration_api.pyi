import typing

import kubernetes.client

class ApiregistrationApi:
    def get_api_group(self) -> kubernetes.client.V1APIGroup: ...
