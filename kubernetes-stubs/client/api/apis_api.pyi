import typing

import kubernetes.client

class ApisApi:
    def get_api_versions(self) -> kubernetes.client.V1APIGroupList: ...
