import typing

import kubernetes.client

class RbacAuthorizationApi:
    def get_api_group(self) -> kubernetes.client.V1APIGroup: ...
