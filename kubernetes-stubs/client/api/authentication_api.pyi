import typing

import kubernetes.client

class AuthenticationApi:
    def get_api_group(self) -> kubernetes.client.V1APIGroup: ...
